---
name: pstack-reflect
description: Review a named session through judgment, tooling and divergent lenses, then propose evidence-backed edits to existing skills. Use when the user says reflect.
---

# Reflect

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/skill:pstack-reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Locate the active transcript

Use the active conversation or an explicitly named host session URI (`history://<id>`) supplied for this task. An explicitly authorized transcript file is also valid. Never scan a transcript directory or infer a current session from timestamps or an opening-prompt search. If the host cannot expose the session, prepare a concise digest from visible messages and label the coverage limitation.

The evidence packet contains user corrections, relevant tool outcomes, touched files and source pointers. Exclude secrets and unrelated private context. The legacy transcript finder is not part of the native workflow.

## 2. Review through three lenses

Read `references/judgment-reviewer.md`, `references/tooling-reviewer.md`, and `references/divergent-reviewer.md`. Preserve all three lenses; they need not consume three simultaneous workers. Use eligible native read-only `reviewer` or `scout` tasks within approved dispatch limits, or apply the lenses locally without claiming independence. OMP owns model and effort.

Supply only the named evidence packet and each template. If a referenced external source lacks authorized access, mark its evidence unavailable rather than changing identities or providers. Results arrive through native task output or the actual child URI.

## 3. Synthesize

Synthesize with `references/synthesizer.md`, including each lens's output. A fresh native reviewer may perform this bounded read-only task if host delegation rules permit; otherwise synthesize locally and say so. Spot-check citations within authorized sources and return Accepted / Rejected / Backlog.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Prepare Backlog items locally. Filing tickets or sending external messages requires user authorization for the target and payload.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit: patch the repository canonical source, preserve its schema and conventions, and use focused trigger/behavior cases plus native discovery checks when authorized.
- `tune description: <skill path>`: make the smallest evidence-backed trigger change and check both positive and negative cases.
- `new native skill: <kebab-name>`: create only after approval, with minimal name/description frontmatter and explicit workflow, authority, evidence and stop rules. Keep canonical source in the repository; user-root installation is separately authorized.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
