### Bug fix

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md). Use configured native roles and real-surface drivers, not foreign tools.

**Own the evidence, plan, review and acceptance.** Each shipped line traces to the demonstrated mechanism. Remove only your hypothesis-driven changes when evidence refutes them; speculative hardening is not a fix.

1. Use the user's reported observation as ground truth, not a check to reconfirm. Establish a local repro on the same surface when needed to isolate the mechanism and prove the eventual correction. Synthesize the trigger or add authorized diagnostics when direct reproduction is unavailable. Ask for human-only control only after stating the exact unreachable surface and evidence already collected. Never bypass auth or touch shared data to reproduce.
2. Binary-search candidate hypotheses. Ground them with `/skill:pstack-how` and `/skill:pstack-why`, choose the most discriminating experiment, observe runtime state, and eliminate. Confirm the surviving mechanism before design/review fan-out. A stubborn hunt uses finite supervised segments and checkpoints from [Autonomous run](autonomous-run.md), not a wake loop.
3. Plan the smallest causal fix. Use `/skill:pstack-architect` across function boundaries. If host rules permit delegation, give a configured native implementation worker explicit paths, original symptom, mechanism, regression acceptance and isolated writer output. A leaf implements its assigned scope and returns it for parent review.
4. After integration, prove the original trigger now passes on the same surface. Quote decisive failure/pass evidence. Unit tests alone do not establish bug absence; wrong-surface or inconclusive stays unverified.
5. Preserve failing-test-first history when a cheap local test exists, per `/skill:pstack-tdd` and `/skill:pstack-principle-sequence-verifiable-units`. Explain when an expensive or unclear integration path makes that cadence inappropriate. Commit only within existing authority.
6. Run [Opening a PR](opening-a-pr.md) only when requested or authorized.

**Reply:** broken behavior, causal mechanism, smallest fix, decisive failing/passing output and real-surface verification limits.
