# Issue desk

A local Python CLI for listing, adding and completing issues. No dependencies, network calls, login, cloud resource or real customer data.

```sh
python3 desk.py --data issues.json list --status open --limit 2
python3 desk.py --data issues.json add 'Review pagination'
python3 desk.py --data issues.json done 2
python3 -m unittest -v
```

`list` returns a JSON array. Pagination is applied within the selected status; an offset is measured in matching issues. `add` and `done` persist to the explicitly selected JSON file. Unknown issue IDs return exit 3 without writing. Invalid input returns a nonzero exit.

Use a disposable data file for mutation checks; preserve the original seed. Verify the actual CLI output and persisted state, not only tests. The maintained example is correct. The fork's `tools/demo.py` prepares a separate synthetic repository with a reproducible pagination regression for a first-use repair exercise; it never modifies this example or an existing nonempty directory.
