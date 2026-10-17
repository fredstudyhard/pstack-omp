### Runtime forensics

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md) for actual native drivers.

**Own the diagnosis. Observe the live mechanism, not just source.** No production fix or PR is implied.

1. Capture an approved live signal: CPU profile for a spin, heap snapshot for a leak, browser/debugger trace for a glitch. Verify target and authority before attaching instrumentation; prefer disposable local reproduction over shared state.
2. Reduce it to the hot path, retainer chain to a GC root or input-free scheduling loop. Large-artifact read-only analysis may use a bounded native scout when host rules permit, with exact artifact paths and a reduced finding rather than bulk output, per `/skill:pstack-principle-guard-the-context-window`.
3. Prove the mechanism with authorized temporary instrumentation using actual debugger/browser tools. Read `xd://eval/browser` before browser eval. A live hotfix or injected script changes process state: use it only within explicit diagnostic authority and document/remove instrumentation owned by this run. Without that authority, remain observational and label the unconfirmed mechanism.
4. Map evidence to source file, symbol and allocation/scheduling line.
5. Keep `throughput checkpoint: n/a, read-only forensics`. Preserve named artifacts under the authorized task directory; do not broaden into home/session scans.

**Reply:** captured signal, reduced finding, causal proof versus hypothesis, source location, artifact paths and limits. Route a requested correction to Bug fix or Perf issue.
