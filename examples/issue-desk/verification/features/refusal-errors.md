# Refusals and storage errors

Users receive nonzero exits and stderr diagnostics for invalid actions or unusable storage, without corrupting issue data.

## Sub-features

- `unknown-id`: absent issue exits 3 without writing.
- `invalid-input`: blank title, negative pagination, invalid status/ID, missing arguments and unknown action exit 2.
- `bad-json`: malformed JSON exits 2 without rewriting it.
- `io-error`: missing parent on add and directory-as-file reads exit 2 without creating storage.

## How to get to it (user POV)

Use the same `python3 desk.py --data "$DATA"` entry point with invalid action arguments, or select a disposable malformed/unwritable path via `--data`.

## Driving it with verify-issue-desk

Preconditions: use only helper-owned synthetic paths, after the mutation group. From the distributed `examples/issue-desk` root, run `python3 verification/scripts/verify.py` to create all paths and retain proof. `BROKEN` denotes its `malformed.json`; `MISSING` its `absent/issues.json`; `SCRATCH` its directory. No chmod or privileged path is needed.

- **Missing issue.** `python3 desk.py --data "$DATA" done 999`: exit 3, stderr `issue 999 does not exist` (`unknown-id`).
- **Blank title.** `python3 desk.py --data "$DATA" add '   '`: exit 2, stderr contains `title must not be blank` (`blank-title`).
- **Negative page.** `python3 desk.py --data "$DATA" list --limit -1` and `python3 desk.py --data "$DATA" list --offset -1`: exit 2 with `limit and offset must be nonnegative` (`negative-limit`, `negative-offset`).
- **Bad choices.** `python3 desk.py --data "$DATA" list --status closed` and `python3 desk.py --data "$DATA" remove`: exit 2, `invalid choice` (`invalid-status`, `unknown-action`).
- **Bad ID.** `python3 desk.py --data "$DATA" done not-an-integer`: exit 2, `invalid int value` (`invalid-id`).
- **Missing argument.** `python3 desk.py --data "$DATA" add` and `python3 desk.py --data "$DATA"`: exit 2, `required` (`missing-title`, `missing-action`).
- **Malformed storage.** Helper writes literal `{not json` plus newline to `BROKEN`; `python3 desk.py --data "$BROKEN" list`: exit 2, `cannot use issue data:` (`malformed-json`).
- **Missing parent.** With `absent/` not created, `python3 desk.py --data "$MISSING" add 'Cannot persist'`: exit 2, `cannot use issue data:`; neither file nor parent is created (`missing-parent-write`).
- **Directory instead of file.** `python3 desk.py --data "$SCRATCH" list`: exit 2, `cannot use issue data:` (`directory-data`). The helper later removes only its own scratch directory.
- **Proof.** Every refusal has empty stdout. The report records exact stderr/exit and byte-identical before/after file contents (or no creation for nonexistent paths), plus cleanup and protected-file checks.

## Gotchas

- argparse includes usage text; verify exit/output/data invariants and retain the actual diagnostic; do not pin library wording.
- JSON parse and OS error wording varies by Python/OS; require the CLI prefix and exact exit code, retain actual diagnostic.
- Directory-as-file and missing-parent checks are deterministic I/O failures, not claims about every permission model.
- Arbitrary structurally invalid JSON, interrupted writes and concurrent same-file mutations are not exhaustively covered. No external service exists to mock or probe.
