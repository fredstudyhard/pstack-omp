### Perf issue

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md) for native driver and role resolution.

**Own the measurement story.** Tie each fix to evidence, not source-reading intuition.

1. Capture a baseline trace on the matching approved surface. Vet it and every later number with `/skill:pstack-benchmark-checklist`.
2. Ground hypotheses with `/skill:pstack-how`. Test mantras cheapest first and stop when an earlier one meets the target.
   1. Don't do unused work.
   2. Don't repeat it.
   3. Do it less.
   4. Do it later.
   5. Do it when the user is not waiting.
   6. Do it concurrently.
   7. Do it cheaper.
   Never claim an unmeasured ceiling.
3. Plan from the trace; use `/skill:pstack-architect` across function boundaries. Delegate only under native host rules with explicit scope and exclusive writer output. Integrate before verification, review the diff and capture a post-fix trace. Each attempt is a verifiable unit per `/skill:pstack-principle-sequence-verifiable-units`.
4. Parse and compare artifacts in a queryable form, such as JSON to SQLite. Control workload and noise. Wrong-surface or inconclusive is not PASS.
5. Record the measured baseline, result, unit and artifact in the delivery or authorized PR.
6. Run [Opening a PR](opening-a-pr.md) only when requested or authorized. Sustained iteration belongs to [Hillclimb](hillclimb.md).

**Reply:** baseline, post-fix result, delta, method caveats and artifact path.
