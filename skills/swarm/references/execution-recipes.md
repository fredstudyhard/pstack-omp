# On-demand team recipes

Use only the shape needed for the requested work. The entrypoint's authority, isolation, project contracts, and acceptance rules apply throughout.

## Frame the shape

- **Coverage:** partition a defined surface into independent slices. Every required slice needs an inspectable result; missing coverage never counts as a pass.
- **Race:** give isolated workers identical briefs. Before launch declare `first pass`, `rank all`, or `best-of`, including acceptance and selection criteria. A fast answer is not a passing answer until its evidence meets the contract.
- **Mixed:** partition coverage and race selected independent slices; declare both required coverage and each race rule up front.
- **Gauntlet:** define ordered gates and their dependencies. Independent read-only lenses may run together; dependent gates wait for the required result. Do not bypass a failed gate by averaging opinions.
- **Exploration:** bound questions, source scope, output cap, and unknowns. Findings do not authorize implementation or replace acceptance evidence.

Use configured native discovery, review, or implementation roles as appropriate, not invented role/model identifiers. Host policy decides model and effort, eligibility, and fan-out size; process remaining slices sequentially when needed. A requested model-family race needs actual identity evidence; unavailable identity fails that family gate closed rather than asserting attribution.

## Launch and isolation

Use the host-supported native task interface for eligible independent slices. Where supported, a single batch uses `tasks: [{task, solutionSpace, name?, agent?}]` and shared `context`; `task` contains owned paths, scope, and acceptance, while `solutionSpace` bounds implementation freedom. Use only configured roles and the host's required default-worker convention. This example is not authority to override host syntax or delegation policy.

Every brief must stand alone. Shared context supplements rather than replaces its goal, ownership, acceptance, stop conditions, and handoff requirements. Native background execution is not filesystem isolation. Writers need disjoint paths or separate worktrees/output directories with a named integration owner; competing race implementations must never edit the same checkout. A non-default branch belongs in that worker's authorized isolated worktree, not the shared checkout.

For measurement or verification, pin exact SHAs/state, method, sample count, sample definition, and order. Only explicitly authorized measurement workers run checks before integration; ordinary implementation workers hand off for the parent's integrated verification.

## Drain and aggregate

Collect terminal results and inspect their evidence. Worker slice reports may use `PASS`, `ISSUES`, or `BLOCKED` under the project convention; these are not whole-task acceptance. A proven defect is `ISSUES`, with every evidenced issue in that slice rather than only the first.

A result missing required state identifiers or method is unusable evidence. If the project retry/deadline policy permits, request one bounded replacement; never automatically widen the contract. After a second miss, or when retry is unauthorized, record the gap. Dropouts allow unaffected independent work to continue, but N-1 results cannot satisfy N required coverage slices.

For coverage, reconcile all required slices and gaps. For races, apply the predeclared first-pass, ranking, or best-of rule to qualifying evidence; isolate or stop unused work under the project lifecycle policy, without hidden residual workers. Parent integration and verification still govern any selected implementation.

Return one consolidated report with a compact slice/result/evidence table when useful, proven issue summaries, gaps/dropouts, unverified state, and the declared race rule and selection rationale when applicable. Do not paste raw worker dumps or let ranking hide a safety or acceptance blocker.
