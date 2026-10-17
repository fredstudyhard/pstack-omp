# List, filter and pagination

Users list issues as JSON, optionally selecting status and paging within that selection without changing storage.

## Sub-features

- `list-all`: default ordered view.
- `list-open-pages`: filter before limit/offset, including the final partial page.
- `list-done`: completed-only view.
- `list-empty`: zero limit, past-end offset and absent-file empty state.
- `list-read-only`: selected file bytes remain unchanged; absent file stays absent.

## How to get to it (user POV)

Use `python3 desk.py --data "$DATA" list` from the project root. Optional flags: `--status open|done|all`, `--limit INTEGER`, `--offset INTEGER`.

## Driving it with verify-issue-desk

Preconditions: doctor passes; `DATA` belongs to this run. For paged cases use the five-row fixture in [README.md](README.md). From the distributed `examples/issue-desk` root, run all cases via `python3 verification/scripts/verify.py`.

- **Empty launch.** `python3 desk.py --data "$DATA" list` before the file exists returns `[]`, exit 0, and creates nothing (`doctor-empty`).
- **All.** `python3 desk.py --data "$DATA" list` returns the complete fixture in order (`list-all`).
- **First page.** `python3 desk.py --data "$DATA" list --status open --limit 2` returns complete rows 2 and 3, not row 5 (`list-open-page-1`).
- **Next page.** `python3 desk.py --data "$DATA" list --status open --limit 2 --offset 2` returns row 5 only (`list-open-page-2`). This distinguishes filtering first from slicing first.
- **Done.** `python3 desk.py --data "$DATA" list --status done` returns rows 1 and 4 (`list-done`).
- **Zero.** `python3 desk.py --data "$DATA" list --limit 0` returns `[]` (`list-zero`).
- **Past end.** `python3 desk.py --data "$DATA" list --offset 99` returns `[]` (`list-beyond-end`).
- **Proof.** All return exit 0, empty stderr, exact expected JSON and unchanged storage bytes. Read the named cases and before/after contents in the retained run's `report.json`.

## Gotchas

- Put `--data` before `list`; otherwise argparse rejects it.
- Offset counts matching rows, not original rows. Mixed statuses in the fixture are essential.
- Default status is all, limit 10, offset 0. Mutation group runs later; do not use its resulting state for fixture expectations.
- Omitting `--data` touches the repository seed for mutations; always supply it.
