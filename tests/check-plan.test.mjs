import { describe, expect, setDefaultTimeout, test } from "bun:test";
import { spawnSync } from "node:child_process";
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

// check-plan.mjs runs under node; a starved CI runner took over bun's 5 s
// default and the test read the killed child as code null (run 36492567721).
setDefaultTimeout(30_000);

const mode = join(import.meta.dir, "../skills/poteto-mode");
const playbook = readFileSync(join(mode, "playbooks/multi-phase-plan.md"), "utf8");
const template = playbook.match(/^````markdown\n([\s\S]*?)^````$/m);
if (!template) throw new Error("Multi-phase playbook has no plan skeleton");
const skeleton = template[1];

function run(plan) {
  const dir = mkdtempSync(join(tmpdir(), "pstack-check-plan-"));
  try {
    const file = join(dir, "plan.md");
    writeFileSync(file, plan);
    const result = spawnSync("node", [join(mode, "scripts/check-plan.mjs"), file], {
      encoding: "utf8",
    });
    return { code: result.status, out: result.stdout + result.stderr };
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
}

function editSection(heading, edit) {
  const start = skeleton.indexOf(heading + "\n") + heading.length;
  const end = skeleton.indexOf("\n#", start);
  return skeleton.slice(0, start) + edit(skeleton.slice(start, end)) + skeleton.slice(end);
}

describe("plan checklists", () => {
  test("the shipped skeleton passes", () => {
    expect(run(skeleton)).toEqual({
      code: 0,
      out: expect.stringContaining("1 PR sections, 0 problems"),
    });
  });

  test("completed boxes remain valid", () => {
    expect(run(skeleton.replaceAll("- [ ]", "- [x]")).code).toBe(0);
  });

  test("a plan saved with a UTF-8 byte-order mark passes", () => {
    for (const plan of ["\uFEFF" + skeleton, "\uFEFF---\ntitle: Plan\n---\n" + skeleton]) {
      expect(run(plan)).toEqual({
        code: 0,
        out: expect.stringContaining("1 PR sections, 0 problems"),
      });
    }
  });

  for (const heading of [
    "### Arm the program",
    "### Spawn owners",
    "### PR mechanics",
    "### Verdict and merge",
    "### Boot recipe",
  ]) {
    test(`${heading} requires work, not just prose`, () => {
      const plan = editSection(heading, (body) => body.replaceAll("- [ ] ", ""));
      const result = run(plan);
      expect(result.code).toBe(1);
      expect(result.out).toContain(`${heading.slice(4)} has no box`);
    });
  }

  test("Close the program requires a checklist", () => {
    const result = run(editSection("## Close the program", () => "\n"));
    expect(result.code).toBe(1);
    expect(result.out).toContain("Close the program has no box");
  });

  test("example boxes cannot replace program tasks", () => {
    const plan = editSection("### Spawn owners", (body) => "\n```markdown\n" + body + "\n```\n");
    const result = run(plan);
    expect(result.code).toBe(1);
    expect(result.out).toContain("Spawn owners has no box");
  });

  test("example boxes cannot replace completion tasks", () => {
    const plan = editSection("## Close the program", (body) => "\n~~~markdown\n" + body + "\n~~~\n");
    const result = run(plan);
    expect(result.code).toBe(1);
    expect(result.out).toContain("Close the program has no box");
  });

  test("program safety controls cannot be replaced by fenced examples", () => {
    const result = run(editSection("### Arm the program", (body) => "\n- [ ] Prepare.\n```markdown\n" + body + "\n```\n"));
    expect(result.code).toBe(1);
    expect(result.out).toContain("Program checklist lacks bounded supervised segment");
    expect(result.out).toContain("Program checklist lacks stop conditions");
  });

  for (const [name, pattern, message] of [
    ["deadline", /^.*\bfinite\b.*\bdeadline\b.*\n/gim, "bounded supervised segment"],
    ["checkpoint", /^.*\bcheckpoint\b.*\n/gim, "explicit checkpoint and resume"],
  ]) {
    test(`missing ${name} safety control fails`, () => {
      const result = run(editSection("### Arm the program", (body) => body.replace(pattern, "")));
      expect(result.code).toBe(1);
      expect(result.out).toContain(`Program checklist lacks ${message}`);
    });
  }

  for (const block of ["Files.", "Build.", "You see.", "Verify, unit.", "Verify, live.", "Verify, perf.", "Review gate.", "Merge."]) {
    test(`missing ${block} block fails`, () => {
      expect(run(skeleton.replace(`**${block}**`, "**Removed.**")).code).toBe(1);
    });
  }

  test("ten numbered live lanes each require an artifact and pass predicate", () => {
    for (const plan of [
      skeleton.replace("- [ ] Lane 10.", "- [ ] Lane 9."),
      skeleton.replace("Save `<evidence-path>`.", "Record evidence."),
      skeleton.replace("Pass when <predicate>.", "Inspect result."),
    ]) expect(run(plan).code).toBe(1);
  });

  test("verification cannot omit live or perf completion", () => {
    expect(run(skeleton.replaceAll("unit, live, and perf boxes are all checked", "unit boxes are all checked")).code).toBe(1);
  });

  test("equivalent verification policy wording is accepted", () => {
    expect(run(skeleton.replaceAll(
      "Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.",
      "Tests alone are insufficient. Verification requires unit, live and perf evidence all complete.",
    )).code).toBe(0);
  });
});

describe("fenced plan evidence", () => {
  for (const [name, open, inner, close] of [
    ["backticks", "```yaml", "message: “code”", "```"],
    ["tildes", "~~~yaml", "message: “code”", "~~~"],
    ["shorter inner backticks", "````markdown", "```yaml\nmessage: “code”\n```", "````"],
    ["shorter inner tildes", "~~~~markdown", "~~~yaml\nmessage: “code”\n~~~", "~~~~"],
    ["different inner delimiter", "```markdown", "~~~yaml\nmessage: “code”\n~~~", "```"],
    ["indented delimiter", "   ~~~yaml", "message: “code”", "   ~~~"],
    ["list item delimiter", "    ```yaml", "    PORT: 3000\n    message: “code”", "    ```"],
    ["longer closing delimiter", "~~~yaml", "message: “code”", "~~~~"],
    ["delimiter with trailing text", "```text", "```still code\nmessage: “code”", "```"],
  ]) {
    test(name, () => {
      const example = `\n${open}\n${inner}\n## Example heading\n${close}\n`;
      expect(run(skeleton + example).code).toBe(0);
      const result = run(skeleton + example + "Prose: “invalid”\n");
      expect(result.code).toBe(1);
      expect(result.out).toContain("curly quote");
      expect(result.out).toContain("mid-sentence colon");
    });
  }
});
