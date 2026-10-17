---
name: pstack-automate-me
description: "Draft or revise a personal native OMP mode skill from explicit preferences and named session evidence. Use for automate me, capture my working style, or update my mode skill."
---

# Automate me

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); it governs tools, roles, authority, budgets and verification throughout this skill.

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

Combine a bounded evidence pass, native skill authoring below, and `/skill:pstack-unslop` for prose discipline.

## Flow

### 0. Check for an existing skill

Inspect the user's named existing mode skill or the applicable native `.omp/skills/` and `~/.omp/agent/skills/` roots for a matching skill, not transcript storage. Follow an existing skill's canonical repository source. Confirm update-versus-new intent with native `ask` only when the user has not already specified it.

- Update the existing skill (default for repeat runs)
- Start fresh (rare, ask why before doing it)

Update mode changes the rest of the flow:
- Step 1 considers only explicitly supplied session evidence since the skill was last edited.
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Use only explicitly named sessions, host-provided `history://<id>` URIs or user-authorized transcript files. Never discover evidence by scanning home session directories or a workspace corpus. If none is available, use this conversation and the direct interview, and state the coverage gap.

For sufficiently large independent slices, native read-only `scout` tasks may examine the supplied evidence within host budget and delegation rules. Otherwise read it locally. Return patterns with exact source pointers, not raw private transcripts. Signals:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Use native `ask` for missing preferences, keeping one focused question at a time and using only its actual supported schema. Offer concrete choices when helpful, then allow free-form corrections.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The **poteto-mode** skill shows the shape. Read it for granularity. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Author a native OMP skill in the user's authorized repository canonical source, with minimal YAML `name` and quoted `description`, and concrete workflow, authority, evidence and stopping rules.

- New personal skills target `~/.omp/agent/skills/<handle>-mode/SKILL.md` only through an explicitly authorized install from that source. Project-only conventions stay in `.omp/skills/<handle>-mode/SKILL.md`.
- Preserve an existing skill's canonical owner and category; never edit an installed copy behind its source.
- Use the user's chosen identifier. Describe `/skill:<handle>-mode` and “work in their style” triggers, not generic coding keywords.
- Do not claim a foreign frontmatter flag changes native discovery. Confirm actual OMP discovery in a fresh process after an authorized install; report NOT_RUN if that invocation is unavailable.

### 5. Iterate on prose

Apply `/skill:pstack-unslop` to every line; keep triggers and executable steps unambiguous.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

Show the canonical diff for approval. Commit, PR, push and user-root installation each require applicable authorization; otherwise leave the source candidate and exact installation instructions. Never write provider settings or secrets.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A mode skill is subjective output. Ask whether the prose matches the user's intent, but also check frontmatter, referenced paths and native discovery when installation is authorized. Do not substitute a subjective review for those checks.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill: author that bounded native skill directly, without history extraction.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.
