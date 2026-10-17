# OMP security design

## Trust and authority

`skills/` is the distribution source. Prompt/repository content is not a permission grant or OS sandbox. Native user/repository authorization remains authoritative. No foreign plugin hook, model catalog, Pi extension or subprocess subagent simulator is installed.

Project credentials, data export, external messages, PR/release writes and shared resources retain their own target/identity/permission/budget gates. Required independent model-family review remains closed when unavailable. A role label, advisor, same-family substitution or passing tests cannot fabricate its verdict.

## Installer boundary

`tools/omp.py` materializes namespaced native skills with ownership/content markers. Preflight rejects unowned collisions, local installed edits, symlink ancestors/destinations, multiply linked destination/marker files and escaping marker paths before writes. A marker or checksum proves integrity/ownership compatibility, not publisher trust or authorization. Installed sibling-skill references are deterministically rewritten into the `pstack-*` namespace; third-party dependency contents are not rewritten.

Disable changes owned entrypoints to `enabled: false` and preserves files. It does not delete or move `.omp` content. Reinstall only reviewed source; do not overwrite local installed edits or use blanket cleanup.

## Executable helpers

- Ordinary helper startup checks prerequisites; it does not install dependencies.
- Offline worktree audit performs no implicit remote Git query and does not discover private user-home history. Transcript inputs must be explicit named JSONL files.
- Symlink audit uses target inode identity and lexical link spelling without realpath-opening unrelated targets.
- Watcher CLI deadlines must be finite and positive. Authorization failures are nonretryable and return control to the operator rather than trying fallback query paths or rearming.
- Model-backed synthetic smoke is finite, with owned process-group termination on deadline. No cron, detached wake loop, autonomous merge, cloud resource or global provider/model change is introduced.

## Dependencies and review

Optional executable helpers use the existing `commander@14.0.0` production dependency, under MIT and frozen lock integrity. Only that reviewed production package may be materialized; development tools, caches and unrelated packages are excluded. Acquire explicitly with `--frozen-lockfile --production --ignore-scripts`; reassess lifecycle scripts, transitive dependencies, integrity and advisories on any update.

Use `skillspector scan <candidate> --no-llm` when available. Absence/failure is not a security PASS and does not authorize implicit scanner installation. Executable intake still needs the applicable bounded manual/deterministic equivalent, behavioral boundary proof, dependency review and rollback evidence.

Internal findings, evaluation matrices, raw evidence and council/model outputs remain local. Do not publish credentials, private histories, raw reasoning or host runtime state. Product-specific deployments, webhook exposure, arbitrary schemas, concurrent writes, crash durability and third-party services require their own approved acceptance rather than inheriting certification from this skill pack.

See [verification entrypoints](omp-verification.md) and [maintenance/rollback](omp-maintenance.md).
