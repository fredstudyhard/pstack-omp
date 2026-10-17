### Session pickup

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md).

**Own the resume point. Read the prior trail instead of redoing it.**

1. Read the explicitly named portable checkpoint, normally `<repository>/.audit/pstack/<task>/checkpoint.md`, or the project's authorized durable handoff path. Read its linked artifacts and bounded decision trail. If the task identifier/path is unknown, inspect only the known repository-local `.audit/pstack/` directory metadata to locate candidate checkpoints, never user-home sessions. For a same-machine locator, `node <absolute-pstack-root>/skills/poteto-mode/scripts/resume.mjs read --project <repository>` reads its Git-local published pointer; diagnose missing, incomplete or mismatched records rather than silently replace them. This convenience locator is not portable persistence. A current-session `history://<id>` or `agent://<id>` supplied by the host may supplement evidence. An earlier transcript requires an explicitly named authorized export; a cloud URL is a source only when accessible under existing authorization, not a native wake/resume feature. No broad session scans.
2. Reconstruct branch, worktree, base/head, landed changes, pending requirements and decisions from the checkpoint plus narrow local git evidence. For human rulings read [the epistemics reference](../../why/references/epistemics.md#claims-about-human-decisions); an agent summary is not an original ruling. A cold-session agent ID is not a live process handle.
3. Compare done versus pending and name the resume point. Do not rerun an already reported failure merely to confirm it or repeat completed investigations. Reassess inherited claims only where current revision, environment or missing evidence affects remaining acceptance.
4. Route to the matching execution, recommendation, ratification or postmortem playbook. Reestablish authority, budget and exclusive writer ownership before continuing. Read-only pickup does not grant implementation, PR creation or landing authority.
5. Verify inherited claims needed for final acceptance on the real artifact per `/skill:pstack-principle-prove-it-works`, without claiming an old self-report is fresh proof. The routed playbook owns remaining execution and required independent review.

**Reply:** prior stopping point, inherited versus redone work, exact resume point, present evidence, missing prerequisites and outcome.
