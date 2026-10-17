### Feature

Read [the OMP runtime contract](../references/omp-runtime.md) first, then [the main entrypoint](../SKILL.md). Short skill names below mean explicit `pstack-` siblings as defined there.

**You own the design, plan, review and acceptance.** Delegate implementation only when host rules permit. A leaf owns its assigned diff and returns it for independent review.

1. Read `../../how/SKILL.md` over the affected subsystem.
2. Read `../../architect/SKILL.md` for competing design exploration. Compare local sketches if independent dispatch is not permitted; do not claim independent evidence.
3. Write the throughput checkpoint as four native todo items, retaining genuinely inapplicable dimensions with `n/a: <reason>`.
   - **Blocking first steps.** Resolve prerequisites before fan-out.
   - **Independent workstreams.** Partition disjoint artifacts; shared writes serialize.
   - **Shared mutable state.** Apply `/skill:pstack-principle-separate-before-serializing-shared-state` before adding locks.
   - **Smallest safe decomposition.** Name why one worker is best when it is.
4. Define the data shape and organizing structure per `/skill:pstack-principle-model-the-domain` before logic. Brief native configured implementation workers with paths, interfaces, chosen shape, exclusions and acceptance. Give every concurrent writer an explicitly created exclusive worktree/output and named base revision. Never invent an isolation parameter or run suites in an active writer's tree. When genuinely distinct designs deserve comparison, use `/skill:pstack-arena` within the dispatch/budget rules. Otherwise implement the scoped conservative design, retaining author/reviewer separation. Use surgical edits, re-ground upstream-derived code, migrate every consumer of shared primitives, and retain attribution.
5. After integration, verify on the matching real surface and every affected consumer. Wrong-surface or inconclusive is not PASS. No mid-flight build/test storm.
6. Shape authorized commits into small ordered units per `/skill:pstack-principle-sequence-verifiable-units`. Do not rewrite unrelated work or publish without authority.
7. If design remains contested, use `/skill:pstack-interrogate`; a required unavailable independent review leaves the gate BLOCKED.
8. Run [Opening a PR](opening-a-pr.md) only when requested or already authorized; otherwise deliver the local artifact and evidence.

Coupled code belongs to one owner. Parent fan-out is for independent artifacts, not competing writers. Rewrite the checkpoint at phase boundaries and give fresh owners consolidated scope.

**Reply:** what you built, what you chose and why, alternatives, throughput checkpoint, real verification and open decisions.
