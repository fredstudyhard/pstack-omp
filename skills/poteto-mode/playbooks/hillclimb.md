### Hillclimb

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md). Use configured native workers, bounded supervised segments and explicit portable checkpoints.

**Own the metric and experimental integrity.** One hypothesis, one measurement, keep or discard. No stacked untested changes or code-inspection wins. One-off improvement uses Bug fix or Perf issue.

1. Ground the workload with `/skill:pstack-how`. Name data size, history, state and concurrency, and reproduce the complaint before choosing the metric. If no case reproduces it, repair the repro rather than hillclimb. Fix one metric, improvement direction and checkable target with minimum attempts when requested. Keep the user's numbers; settle material missing targets before the run. A minimum-attempt requirement never overrides budget or safety stops.
2. Build a sensitive harness per `/skill:pstack-principle-build-the-lever`. Demonstrate realistic contrasting workloads separate, vet with `/skill:pstack-benchmark-checklist`, then freeze it. One repeatable command prints metric, error count and work count; use repeated samples such as median of N. Record baseline and a green regression gate before changes.
3. Open `/skill:pstack-show-me-your-work` and place ignored transient `decision.tsv` under `<repository>/.audit/pstack/<task>/`. Columns are id, hypothesis, change, before, after, delta, tests, kept/reverted, note. Read it before each attempt. Do not store private transcripts or credentials.
4. Ground each hypothesis in a specific mechanism from step 1. For perf, use the mantra order in [Perf issue](perf-issue.md), not its early-stop rule.
5. Iterate one hypothesis at a time.
   - Delegate only when host rules permit, using a configured implementation worker, tight paths and exclusive worktree/output. Independent hypotheses may run together only within the approved dispatch ceiling and without shared writes.
   - Integrate the selected attempt, measure frozen before/after and run the regression gate. No suites against active sibling edits.
   - Keep only an improvement beyond noise with green regression evidence. Discard the attempt's changes otherwise, preserving unrelated work.
   - With commit authority, make one commit per accepted fix and stage named files, never `git add -A`. Log kept and discarded attempts alike.
   Each iteration is a verifiable unit per `/skill:pstack-principle-sequence-verifiable-units`. At the supervised deadline/call boundary, checkpoint target, baseline, attempts, artifacts, current revision and next hypothesis. Resume explicitly under OMP; no background wake mechanism exists.
6. On a plateau, pivot category, combine evidence from near-misses or re-read the source. Correctness and simplicity outrank the number. Reject behavior regressions and keep a simplification that holds the metric.
7. Finish when the predicate is met, or report a genuine dead end or marginal remaining ideas without relaxing it. Cheap untried hypotheses remain pending at a budget boundary, not falsely completed.
8. Run [Opening a PR](opening-a-pr.md) for accepted ordered commits only within publication authority.

**Reply:** metric and target, baseline/final and percent delta, attempts kept/discarded, accepted fixes, decision-log path, predicate state and strongest next idea.
