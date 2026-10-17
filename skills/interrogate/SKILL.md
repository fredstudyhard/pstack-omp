---
name: pstack-interrogate
description: "Use for bounded code review, PR/final review, correctness, performance, migration or public-contract review; also explicit deep, adversarial or multi-model review, interrogate, challenge this, stress test this code, find blind spots or tear this apart. Ordinary review stays bounded; independent model fanout is opt-in."
---

# Interrogate

First read the [OMP runtime contract](../poteto-mode/references/omp-runtime.md); actual host policy, tool schemas, delegation gates and configured model roles remain authoritative. This is the canonical engineering code-review entrypoint, not permission to edit or launch providers.

## Choose the review mode

- **Normal (default):** one bounded review using the native `reviewer` role when host delegation gates permit. Otherwise inspect directly and identify the lack of independent review. Do not launch one reviewer per model, multiple workers or a council for an ordinary review.
- **Explicit deep/adversarial:** read [the adversarial playbook](references/adversarial-review.md) only when the user requests deep review, adversarial challenge or multi-model coverage. A deep review can use one reviewer; adversarial intent alone does not authorize multi-model fanout. Use independent families only when requested or required by an applicable host gate, and only within actual delegation and budget authorization.
- **Security scope:** keep `security-review` independent. Invoke it and the native `security-reviewer` role when appropriate for auth, permissions, secrets, untrusted input, dependencies, deployment exposure, MCP or agent/tool boundaries; do not add a security lane to unrelated changes.
- Use native `scout` only for a permitted bounded, independent read-only evidence check. The coordinator owns final proof. A bounded `advisor` opinion may inform a high-impact disagreement, but neither it nor continuous advisor output replaces file inspection or a required fresh independent verdict.

Never change provider enablement, presets or agent schemas to obtain a review. Missing a specifically required reviewer/family is a blocked gate, not permission to substitute another lane.

## Shared review procedure

Apply this procedure in every mode; delegated reviewers receive the same requirements and [finding/evidence contract](references/review-contract.md).

1. Identify review shape, exact scope, requirements, non-goals and known verification. State the intended behavior before judging implementation. Resolve intent from available evidence; ask only when material uncertainty remains.
2. Pin the target revision/base. Read the real diff and changed files, not just a summary. Use user-specified files or diff; for a branch review establish the appropriate base before collecting its full changeset. For recent work, identify the actual affected files.
3. Check requirement compliance before style or polish. Inspect adjacent interfaces receiving or routing changed values. For every new type, command, event, message or enum crossing a module boundary, inspect the consuming dispatch point: silent fallthrough, discard or an unhandled branch can be an integration defect.
4. Trace changed values through boundaries, persistence, error paths and external side effects. Broaden the read scope only for a named concrete risk, not a default repository crawl.
5. Report actionable, unintentional issues introduced by the change, with patch-anchored evidence, a plausible trigger and concrete impact. Apply the shared evidence bar; do not manufacture findings to fill a review.
6. Remain read-only: no edits, destructive commands, provider/network identity calls or other side effects by default. Run only explicitly authorized, named targeted checks necessary to interpret a claim; do not trigger builds or edits merely to strengthen a theory. Report existing verification separately from checks actually run.
7. Stop and mark the review **incomplete** if the diff, target files or required deployment facts are unavailable. Name missing proof; never fabricate a verdict from a label, task name or external reviewer output. If required independent evidence is unavailable, mark that gate **BLOCKED** and retain only honestly bounded partial coverage.

## Deliverable

Use the [finding schema and verdict rules](references/review-contract.md). Include intent and requirements, revision/base and files reviewed, actionable findings, verification actually run, missing proof and residual risk. No findings is valid. Do not claim correctness or merge readiness while required evidence is incomplete. Explicit adversarial review adds the synthesis and attribution sections from its playbook; it does not replace this shared contract or auto-apply fixes.
