### Trace forensics

Read [the OMP runtime contract](../references/omp-runtime.md) first and [the main entrypoint](../SKILL.md).

**Own the diagnosis from the fixed artifact.** Unlike Runtime forensics, do not rerun the capture or mutate the target.

1. Identify the supplied format and choose an existing parser: DevTools/trace tooling for cpuprofile or compressed JSON, text for spindump, heap tools for heapsnapshot. Read only named artifacts. Large-artifact analysis may use a bounded native read-only scout under host delegation rules per `/skill:pstack-principle-guard-the-context-window`.
2. Transform into a queryable shape, such as SQLite rows per sample, frame or node. Put derived artifacts in the authorized task directory and preserve the original bytes.
3. Narrow by time-holding frames and call trees; for leaks follow retainers to a GC root; for spindumps identify the hot/blocked thread and wait reason.
4. Attribute to source file, symbol and line using captured symbols. Resolve missing mappings if available, otherwise state plainly that source attribution remains missing.
5. Compare a supplied paired capture when available. Without independent confirmation, label the strongest supported hypothesis rather than assert a confirmed cause.
6. Return a cited diagnosis. Keep `throughput checkpoint: n/a, read-only forensics`. No fix, PR, new live capture or broad transcript scan unless separately requested. Route a requested correction to Bug fix or Perf issue.

**Reply:** artifact/format, reduced finding, source attribution, derived artifact paths and whether a paired capture confirmed it.
