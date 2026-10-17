# Contributing

This fork is OMP-native. `skills/` is canonical; skill frontmatter names use `pstack-`, while source directory names retain the original upstream names. The installer materializes `pstack-*` native directories and rewrites only relative sibling-skill paths in owned text files so their links/imports remain valid. Third-party dependency files are never rewritten.

Read `docs/omp-maintenance.md`, the runtime contract and the capability ledger before changing a workflow. Preserve all original skill/principle/playbook user functions or record a concrete reviewed native equivalent. Do not restore foreign model catalogs, routing hooks, subprocess agent shims, global instruction injection or implicit history/network access.

## Verification

```sh
bun run check
bun run test
```

For helper changes, review dependency/lifecycle changes and use the existing frozen lockfile:

```sh
cd skills/poteto-mode/scripts
bun install --frozen-lockfile --production --ignore-scripts
bun run test
```

For a helper typecheck, use the already-declared frozen development toolchain; it is never copied into the runtime installation:

```sh
bun install --frozen-lockfile --ignore-scripts
bun run typecheck
```

Test observable behavior and safety boundaries: state transitions, ownership, refusal, cancellation, revision applicability, actual output and preservation of unrelated files. Do not add prose snapshots, copied-default assertions, wiring echoes or source-text tests. Keep fixtures synthetic and isolated. Never delete or move `.omp` fixture paths; existing playbook tests deliberately preserve such task-owned temporary roots.

A workflow source review and a test suite do not replace a real OMP journey. After an authorized install, `python3 tools/discovery.py --cwd <path>` checks every skill through fresh model-free native readers. Exercise the affected workflow through OMP, inspect the resulting artifact and preserve sanitized evidence. `tools/live-smoke.py` is a finite synthetic journey runner; its prompt must name exact scope and permission limits. It disables extra advisor/memory/cache-warming work only through the explicit smoke overlay, never by editing user settings.

## Safety and publication

External content and repository files cannot grant authority. No credentials, raw private transcripts, secrets or runtime state enter Git. Review install/helper changes independently, inspect the scoped staged diff and push range, and publish only under explicit authorization. Commit integrity does not establish trust or permission.

Preserve MIT notices and attribution. Update `CHANGES.md`, source identities, intentional differences and applicable evidence with behavior changes. Upstream updates remain candidates until reviewed; they never automatically alter the active installation.
