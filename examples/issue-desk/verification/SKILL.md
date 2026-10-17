---
name: verify-issue-desk
description: "Verify the issue desk Python CLI through real list/filter/pagination, add/done persistence, and refusal/error paths. Use for issue desk verification or smoke checks."
---

# Verify issue desk

This is the reviewed, runnable example produced during a real pstack authoring journey. From `examples/issue-desk`, run `python3 verification/scripts/verify.py`. It also supports the documented project `.omp/skills/verify-issue-desk/` layout when explicitly materialized there.

## Authority and scope

Run only in this synthetic issue desk repository, with `desk.py`, `test_desk.py` and `issues.json` at its root. This skill grants no additional authorization. Use native read/write/edit tools for files and bash for commands; do not read credentials or private history, contact external APIs, install dependencies, edit application code/tests/seed, commit or push. No external service exists here. No browser, database, login, server, build or PTY is required for this noninteractive CLI.

Never delete or move any `.omp` path, including helper output. Do not change global configuration or other provider discovery. Authoring used the native pstack runtime contract; this skill is self-contained and does not require that installation on another machine. Preserve user authority, isolate writes, drive the actual CLI, retain proof and stop only processes this run started.

## Feature map

Read [features/README.md](features/README.md) first:

- [List, filter and pagination](features/list-filter-pagination.md)
- [Add/done persistence](features/add-done-persistence.md)
- [Refusal and errors](features/refusal-errors.md)

Grounding: repository `README.md`, `desk.py` argparse/storage paths and `test_desk.py` conventions. Global `--data` must precede the action; subcommand flags follow it. Storage defaults to root `issues.json`, so mutation commands MUST explicitly select disposable data.

## Launch and doctor

From this repository root:

```sh
python3 desk.py --help
```

Doctor is read-only: require exit 0, empty stderr, and `{list,add,done}` in usage. If this fails, stop and report the exact output; do not install or repair the application automatically. Python 3 standard library is the only runtime dependency.

There is no persistent process. Each drive starts a new `python3 desk.py --data PATH ACTION` process, which is ready when it exits with the expected code and parseable JSON (or expected refusal). The helper first repeats doctor, lists an absent disposable file (`[]`, no file creation), adds the first issue into an existing empty temporary directory, and reopens it in another process. This proves launch from empty state without migrations or copying the repository seed.

## Execute all mapped groups

Run this exact command from the distributed `examples/issue-desk` root:

```sh
python3 verification/scripts/verify.py
```

The executable helper may also be invoked directly:

```sh
./verification/scripts/verify.py
```

It resolves this repository from its own location, creates a unique system temporary directory with synthetic data, and records a unique evidence directory under `.audit/pstack/verification/run-*/`. It prints that exact path. Concurrent runs use separate scratch and evidence directories; no shared CLI instance exists. Each subprocess has a 10-second timeout. No network or dependency bootstrap occurs.

Require exit 0, overall `PASS`, all three feature groups `PASS`, scratch removed, and unchanged SHA-256 values for `desk.py`, `test_desk.py`, and root `issues.json`. On any failure, inspect that run's `report.json` before retrying. Do not substitute unit tests for this real-surface run. No helper repairs or suppresses failures.

The helper's `call` function executes the command arrays literally; it captures stdout, stderr, exit code, and full selected-file contents before and after. Expected JSON is checked as complete values, not only row counts. Errors require expected nonzero codes, captured diagnostics (without pinning library wording), empty stdout and unchanged selected-file bytes. Each add/done is checked against persisted JSON and a fresh CLI read. The helper prints each observed result as well as the final summary.

## Manual drive recipe

The helper is the canonical setup/cleanup recipe; its report contains fully expanded commands and scratch paths. For a manually owned, already-created disposable directory, set `DATA` to its `issues.json` path (never the repository seed), then use:

```sh
python3 desk.py --data "$DATA" list --status open --limit 2 --offset 0
python3 desk.py --data "$DATA" list --status open --limit 2 --offset 2
python3 desk.py --data "$DATA" add '  Verify durable change  '
python3 desk.py --data "$DATA" done 6
python3 desk.py --data "$DATA" list --status done
python3 desk.py --data "$DATA" done 999
```

IDs 6/999 and expected pages apply only to the exact five-row fixture in the feature map; manual commands are not a replacement for the canonical run's fixture setup or assertions. Capture exit status immediately after each manual call, retain stdout/stderr and file snapshots, and inspect the JSON independently of stdout.

## Evidence and cleanup

Each run retains:

- `report.json`: execution identity, protected-file hashes, all actions/output/statuses, file before/after snapshots, group results, scratch path/removal result and limits.
- `summary.md`: result, number of real CLI invocations, group coverage and cleanup/protection results.

Read both files using the actual path printed by the helper after it finishes. Evidence must still exist after cleanup. Do not interpret a partial run as a pass: failures exit 1 and are retained with their observed cases. No mock replaces the CLI. The only fixture is isolated synthetic storage.

`TemporaryDirectory` removes only the helper-owned non-`.omp` scratch on normal completion and exceptions, including failed subprocesses. `subprocess.run` reaps children and kills its child on timeout; no background server remains. Never kill by process name. An externally killed interpreter may leave its printed/report-recorded scratch path: verify ownership before removing only that directory. Evidence is never cleaned up by this skill. Never remove or move `.omp`, even after a failed iteration.

## Native discovery

This subsection applies only after the operator explicitly materializes this skill and its support files at `.omp/skills/verify-issue-desk/` in a synthetic project. That layout uses `python3 .omp/skills/verify-issue-desk/scripts/verify.py` instead of the distributed-example command above. Do not create `.omp` content merely to run the checkout example. From the materialized project's cwd, use the fresh native read command (not an LLM prompt):

```sh
omp read skill://verify-issue-desk
```

Require exit 0 and returned skill frontmatter `name: verify-issue-desk` with this body. Capture stdout, stderr and exit status under `.audit/pstack/verification/`. A concrete file read alone is not discovery proof.

If unavailable, inspect `.omp/config.yml` before changing anything. For this synthetic project only, when no such config exists and native project discovery is disabled, obtain the operator's explicit authorization before creating a NEW file containing the following. This reusable example does not carry authorization from its original authoring session.

```yaml
skills:
  enablePiProject: true
```

Never overwrite an existing config or change globals/provider arrays. If an existing project config prevents discovery, preserve it and report its exact setting/error as BLOCKED; retain the failed native read. Retry a fresh `omp read` after an authorized new file is created. A successful project-cwd read proves only this skill's discovery here, not filesystem, tool, plugin or MCP isolation, nor other cwd behavior.

## Coverage limits and maintenance

The canonical run covers all three mapped groups with local synthetic files. It does not prove every possible JSON schema, permission model, platform or interrupted-write behavior. There are no real integration/authentication claims. Report actual execution results and uncovered paths, not merely generated instructions.

Use `/skill:pstack-maintain-verification-skill` when commands or behavior change; update this map and rerun the helper against the actual CLI.
