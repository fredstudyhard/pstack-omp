# Issue desk verification map

## Baseline preconditions

From the distributed `examples/issue-desk` root, run `python3 desk.py --help`, then `python3 verification/scripts/verify.py`. Python 3 standard library only; no service or installation. Read [the skill](../SKILL.md) for authority, launch, doctor, evidence, cleanup and the conditional explicitly materialized `.omp` layout.

The helper starts with an absent file to prove empty-state launch, then writes its own fixture into its unique system temporary directory. It never copies or changes root `issues.json`.

| ID | Title | Status |
| --- | --- | --- |
| 1 | Closed investigation | done |
| 2 | Fix search | open |
| 3 | Document launch | open |
| 4 | Old release | done |
| 5 | Verify handoff | open |

## Driving conventions

`DATA` in the maps denotes only the helper-owned scratch `issues.json`, never the root seed. `python3 desk.py --data "$DATA"` is the exact user entry point. Feature files show literal action arguments; the helper supplies fully resolved paths and Python interpreter. Groups execute in index order. Persistence tests add ID 6, then finish it; refusal tests start from that completed state. Separate runs never share data.

## Proof and skip reporting

Require exit 0 for successful actions, exact JSON output, empty stderr, persisted file state and independent fresh-process reads. For refusals require the specified exit, empty stdout, expected stderr, and unchanged bytes (or no file creation). Capture actual command/output/file snapshots in `report.json`; do not treat test-suite results as CLI proof. Preserve `.audit/pstack/verification/run-*/report.json` and `summary.md` after scratch cleanup. Missing proof is NOT_RUN/BLOCKED, never PASS. Discovery is a separate fresh `omp read skill://verify-issue-desk` gate.

## Features

- [List/filter/pagination](list-filter-pagination.md): all/open/done views, filtering before offset/limit, empty pages and no writes.
- [Add/done persistence](add-done-persistence.md): empty-start creation, trimmed title/ID allocation, cross-process persistence, completion and repeat completion.
- [Refusal/errors](refusal-errors.md): missing IDs, invalid arguments, malformed storage and I/O failures with unchanged files.
