# Add and complete issues durably

Users add an open issue, then complete it; output agrees with stored JSON and later CLI reads.

## Sub-features

- `add-empty`: absent file in an existing directory becomes valid storage with ID 1.
- `add-normalize`: trim title, allocate next ID and preserve prior issues.
- `add-reopen`: a separate CLI invocation reads the new issue.
- `done-persist`: completion persists and changes open/done views.
- `done-repeat`: completing an already-done issue succeeds without changing file bytes.

## How to get to it (user POV)

Use `python3 desk.py --data "$DATA" add 'title'` or `python3 desk.py --data "$DATA" done INTEGER` from the root.

## Driving it with verify-issue-desk

Preconditions: doctor passes. From the distributed `examples/issue-desk` root, run `python3 verification/scripts/verify.py`; it creates its own scratch directory, isolates all writes and prepares/resets its fixture.

- **Empty creation.** On an absent file, `python3 desk.py --data "$DATA" add '  First synthetic issue  '` returns and persists exactly `{"id":1,"title":"First synthetic issue","status":"open"}`. A new `python3 desk.py --data "$DATA" list` returns that single row (`empty-add`, `empty-reopen`).
- **Add to fixture.** After the helper installs the five-row fixture, `python3 desk.py --data "$DATA" add '  Verify durable change  '` returns ID 6, title `Verify durable change`, status `open`. Disk contains all previous rows unchanged plus that object (`add-persist`).
- **Reopen.** `python3 desk.py --data "$DATA" list --status open` returns IDs 2, 3, 5, 6 with exact titles/statuses (`add-reopen`).
- **Complete.** `python3 desk.py --data "$DATA" done 6` returns that object with status `done`; stored JSON agrees and preserves the other five rows (`done-persist`).
- **Fresh views.** `python3 desk.py --data "$DATA" list --status open` returns IDs 2, 3, 5; `python3 desk.py --data "$DATA" list --status done` returns IDs 1, 4, 6 (`done-open-view`, `done-closed-view`).
- **Repeat.** `python3 desk.py --data "$DATA" done 6` succeeds with the same completed object and unchanged stored bytes (`done-repeat`).
- **Proof.** Every call exits 0 with empty stderr. Inspect exact stdout and stored before/after contents in the run's `report.json`; summary must show this group PASS and root seed/application/tests unchanged.

## Gotchas

- IDs depend on current maximum, not list length. This fixture makes the expected new ID exactly 6.
- Parent directories are not auto-created; empty-launch proof uses an existing temporary directory.
- Repeat completion is not an unknown-ID refusal; it is a successful operation.
- Do not manually reset root seed. Only the helper's owned scratch fixture is reset between empty-start and seeded checks.
