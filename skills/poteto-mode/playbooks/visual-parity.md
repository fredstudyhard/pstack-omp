### Visual parity

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md). Read images with native `read` before describing them; obtain configured designer judgment before visual implementation or approval.

**The immutable baseline is the spec.** Image diff, not eyeballing, establishes pixel equivalence.

1. Before migration, capture a visual regression baseline covering component states and both implementations when matching two. No baseline means no parity claim.
2. Hold the anti-shortcut clauses: no harness changes, baseline tampering or component restructuring to force a pass. A wrong baseline requires an operator decision, not an edit.
3. Migrate shared primitives first, then one component per verifiable unit. Concurrent writers require exclusive worktrees/output, named bases and an integration owner per `/skill:pstack-principle-separate-before-serializing-shared-state`.
4. After integration, drive the actual matching surface and compare against baseline. Investigate every nonzero pixel delta. Iterate within the explicit call/time budget; at a boundary checkpoint the remaining delta and next action, never silently loosen the zero-diff predicate or install a wake loop.
5. Run [Opening a PR](opening-a-pr.md) per safe authorized batch only when requested or authorized.

**Reply:** components migrated, diff per component, baseline harness path, image evidence, designer judgment and remaining work or blocked gates.
