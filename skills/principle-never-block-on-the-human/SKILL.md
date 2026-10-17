---
name: pstack-principle-never-block-on-the-human
description: "Apply when tempted to ask 'should I do X?' on reversible work."
user-invocable: false
---

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md).

# Never Block on the Human

Within the user's authorized scope, keep reversible implementation work moving and let the human course-correct. Evidence-backed execution choices usually cost less than unnecessary confirmation.

- Proceed on authorized reversible work, then present the result. Product direction, external writes, credentials, cost and irreversible actions still require their applicable approval.
- When a problem is within scope, fix its cause. Otherwise report it without expanding the task.
- Irreversible actions (force-push, delete production data, send external messages) still require confirmation.
- Reversible actions (write code, edit notes, split tasks) within the authorized task should proceed without unnecessary confirmation.
- Product direction comes from the human. Execution should not block.
