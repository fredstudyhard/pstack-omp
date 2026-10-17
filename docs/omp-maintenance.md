# Maintenance and rollback

## Ownership

`skills/` is the only active distribution source. `tools/omp.py` installs its reviewed contents into native OMP user skills. Names are prefixed to avoid existing bare-name collisions. Other-runtime plugin manifests, model catalogs, hooks and subagent launchers are not part of this fork's runtime.

Installed files are materialized copies with an ownership/content manifest, not a second canonical source. Edit the repository, not installed copies. Installer preflight refuses unowned collisions, symlink targets, path traversal and local installed edits before writing. If the source changed, inspect it and re-run checks/security review before installing it; the ownership marker is not a trust verdict.

## Local verification

```sh
bun run doctor
bun run check
bun run test
python3 -m unittest discover -s examples/issue-desk -p 'test_*.py' -v
```

Optional PR/orchestration helpers have their own pinned lockfile. Inspect dependency/lifecycle changes first, then explicitly install without lifecycle scripts:

```sh
cd skills/poteto-mode/scripts
bun install --frozen-lockfile --production --ignore-scripts
bun run test
```

No helper should install dependencies merely because a skill was read. `bun`, `gh`, source-control permission and the correct repository are prerequisites only for workflows that use them. Tests use disposable synthetic repositories and no provider credentials. Live OMP checks are separate from tests and require an approved model-plan/call/time budget.

## Review upstream as a candidate

1. Read `tools/omp-provenance.json` for immutable original/port pins. Read source release notes and the new commit's license/dependency changes. A newer revision alone is not a reason to activate it.
2. Fetch the public `upstream` remote into a review-only ref/object, without merging or checking it out over this branch. Verify its URL is `https://github.com/michael-denyer/pstack-claude.git` first. Do not follow untrusted replacement remotes or recursively initialize submodules.
3. Compare the recorded port commit with the full candidate SHA. Review changed `plugins/pstack/skills/<name>/` against this fork's `skills/<name>/`; compare host adapters only for useful behavior, never re-enable their mechanisms. Original Cursor changes are reviewed against the separately recorded original pin.
4. Use a separate candidate checkout/branch. Preserve unrelated changes and isolate concurrent writers. No automatic update script changes the active installation. Record each accepted/rejected semantic difference in `omp-porting.md` and affected capability rows.
5. Review prompts, all executable task/fixture/grader/helper changes, dependencies, outbound endpoints, history/credential access and permissions. If available, run `skillspector scan <candidate> --no-llm`; otherwise require equivalent bounded deterministic/manual review. Scanner failure/absence is not PASS.
6. Run applicable tests, source/link checks, fresh native discovery, affected real-path smoke and required independent review. Bind evidence to candidate content/revision. A later change invalidates any verdict whose applicability no longer holds.
7. Update provenance, manifest, capabilities, changelog and evidence. Inspect the scoped staged diff and pending push range before an authorized push; verify the resulting remote revision. Do not include host settings, raw sessions, credentials, private artifacts or unrelated changes.
8. Only then run the explicit installer and repeat native discovery in each supported cwd. A checked-out candidate is not installed behavior.

## Disable and restore loadability

```sh
python3 tools/omp.py disable
```

This edits owned entrypoints to `enabled: false`, keeps files/evidence and deletes/moves nothing. Prove that a fresh OMP process no longer resolves the fork's names; existing sessions may retain the old loaded registry until restarted.

To re-enable the reviewed version:

```sh
python3 tools/omp.py install
```

For a previous version, choose a separately inspected checkout at the desired known commit and run its installer against the same native root. Disable first if a current failure could affect new sessions. Never reset this checkout over user changes, delete the `.omp` tree, overwrite local installed edits or silently enable another provider. Permanent removal of exact `.omp` paths requires separate explicit user authorization.

## Persistent records

Repository provenance and sanitized verification are the durable source for this fork. A session-local `agent://` or `history://` is never its only handoff reference. When `OBSIDIAN_VAULT` is unavailable, do not guess or write a vault path. This is a feature task, not a host rebuild; no rebuild record is implied. Promote stable cross-project conclusions through the governed vault workflow only when its environment and authorization are available.
