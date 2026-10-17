# Behavior-preserving code-slop lens

Inspect only the authorized diff and enough surrounding code/callers to establish local conventions and behavior. Code style is not evidence of authorship. Do not introduce a second convention.

Candidates, not automatic deletions:

- Comments that repeat code or conflict with local style: retain rationale, constraints, safety explanations, and public contracts.
- Defensive checks or try/catch on trusted paths: remove only when the trust boundary and equivalent error behavior are established. Apparent redundancy is not proof.
- Casts to `any` bypassing type issues: express the actual type or narrowing without changing supported inputs or runtime behavior; do not hide the issue with a different escape hatch.
- Deep nesting: use early returns only when control flow, cleanup, ordering, and side effects remain equivalent.
- Other diff-introduced patterns inconsistent with surrounding code: prefer the existing idiom when it is correct, not a broad restyle.

Keep required validation, diagnostics, error handling, and tests. Do not fix unrelated bugs under cleanup authority. If equivalence cannot be established, leave the code and report the uncertainty. Name the project-defined regression checks needed; run them only when assigned/authorized under the host verification policy. A smaller diff is not proof of unchanged behavior.
