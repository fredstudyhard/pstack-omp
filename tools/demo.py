#!/usr/bin/env python3
"""Prepare an isolated local repository for the pstack first-use journey."""
import argparse
import json
from pathlib import Path
import shlex
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROMPT = 'The issue desk list command returns only one open issue with --status open --limit 2 even though three open issues exist. Reproduce it through the real CLI, find and fix the cause without changing the test expectations, and verify pagination and persistence. Use pstack-poteto-mode. Do not commit, push, contact external services or read outside this synthetic repository.'
GOOD = "            selected = [issue for issue in issues if args.status == 'all' or issue['status'] == args.status]\n            result = selected[args.offset:args.offset + args.limit]"
BAD = "            selected = issues[args.offset:args.offset + args.limit]\n            result = [issue for issue in selected if args.status == 'all' or issue['status'] == args.status]"


def prepare(destination=None):
    destination = Path(destination) if destination else Path(tempfile.mkdtemp(prefix='pstack-issue-desk-'))
    if destination.exists() and any(destination.iterdir()):
        raise ValueError(f'refusing nonempty demo destination: {destination}')
    destination.mkdir(parents=True, exist_ok=True)
    source = ROOT / 'examples/issue-desk'
    for name in ('desk.py', 'test_desk.py', 'README.md'):
        shutil.copy2(source / name, destination / name)
    app = destination / 'desk.py'
    text = app.read_text()
    if text.count(GOOD) != 1:
        raise ValueError('demo seed no longer matches the maintained application; review the regression fixture')
    app.write_text(text.replace(GOOD, BAD))
    seed = [
        {'id': 1, 'title': 'Closed investigation', 'status': 'done'},
        {'id': 2, 'title': 'Fix search', 'status': 'open'},
        {'id': 3, 'title': 'Document launch', 'status': 'open'},
        {'id': 4, 'title': 'Old release', 'status': 'done'},
        {'id': 5, 'title': 'Verify handoff', 'status': 'open'},
    ]
    (destination / 'issues.json').write_text(json.dumps(seed, indent=2) + '\n')
    (destination / '.gitignore').write_text('__pycache__/\n.audit/\n')
    commands = [
        ['git', 'init', '-b', 'main'],
        ['git', 'config', 'user.name', 'Pstack Demo'],
        ['git', 'config', 'user.email', 'demo@example.invalid'],
        ['git', 'add', 'desk.py', 'test_desk.py', 'README.md', 'issues.json', '.gitignore'],
        ['git', 'commit', '-m', 'Seed local issue desk'],
    ]
    for command in commands:
        subprocess.run(command, cwd=destination, check=True, capture_output=True, text=True, timeout=15)
    return destination.resolve()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path)
    args = parser.parse_args()
    destination = prepare(args.destination)
    print(json.dumps({'workspace': str(destination), 'data': 'synthetic local files only', 'prompt': PROMPT, 'commands': [f'cd {shlex.quote(str(destination))}', 'python3 desk.py list --status open --limit 2', 'omp ' + shlex.quote('/skill:pstack-poteto-mode ' + PROMPT)]}, indent=2))


if __name__ == '__main__':
    main()
