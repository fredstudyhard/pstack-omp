---
name: pstack-no-comments
description: "Spawn the comment-sicko subagent, fix accepted findings, and offer encodings for claimed constraints."
---

# No comments

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

Spawn comment-sicko. Act on accepted findings.

Defer to comment-sicko's fresh perspective.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Steps

1. Dispatch a fresh native `reviewer` using `task`, with the exact read-only scope and instructions to read [`../poteto-mode/references/agents/comment-sicko.md`](../poteto-mode/references/agents/comment-sicko.md). Request findings and a proposed comment-only diff, not workspace writes; the parent applies accepted changes and owns application-code fixes. OMP owns model and effort. If the required independent reviewer cannot run, report BLOCKED rather than self-certifying.
2. Inspect the report and proposed diff. Reject application-code edits, scope escapes, exception-protected deletions and unsupported `MUST KILL` claims. For thin `IMPORTANT` or `do not remove` judgments, use `/skill:pstack-how` or `/skill:pstack-why` on the symbol. Preserve safety/legal/owner constraints and ambiguous keeps until evidence resolves them. Audit scoped lint and TypeScript suppressions for real underlying defects; do not erase their protection without a proven replacement. Allow one corrected reviewer report within budget; a second rejected report leaves the gate open, not passed.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, run `/skill:pstack-architect` once for the accepted set and surrounding code. Stop at the sketch. Architect shapes. Step 4 implements.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The **principle-fix-root-causes** and **principle-redesign-from-first-principles** skills guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Preserve constraints and exceptions until their owner or authorized user approves a proven replacement. Offer the cheapest in-scope type, runtime, test or CI encoding. If approved, encode then delete the redundant comment. Otherwise keep it and report the unresolved constraint; unattended operation is not approval.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.
