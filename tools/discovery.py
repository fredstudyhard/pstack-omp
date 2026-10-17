#!/usr/bin/env python3
"""Resolve every installed pstack skill in fresh OMP read processes; no model prompt."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

from omp import ROOT, inventory


def inspect(cwd):
    expected = {name for name, _ in inventory()}
    resolved = []
    failures = []
    for name in sorted(expected):
        result = subprocess.run(['omp', 'read', 'skill://' + name], cwd=cwd, capture_output=True, text=True, timeout=20)
        text = result.stdout + result.stderr
        match = re.search(r'\[Skill file: ([^\n]+)\]', text)
        if result.returncode != 0:
            failures.append({'name': name, 'error': text.splitlines()[0] if text else f'exit {result.returncode}'})
        elif not match:
            failures.append({'name': name, 'error': 'resolved source identity unavailable'})
        else:
            actual = Path(match[1])
            intended = Path.home() / '.omp/agent/skills' / name / 'SKILL.md'
            if actual != intended:
                failures.append({'name': name, 'error': 'unexpected source', 'source': str(actual)})
            else:
                resolved.append(name)
    return {'cwd': str(Path(cwd).resolve()), 'status': 'PASS' if not failures else 'FAIL', 'resolved': resolved, 'failures': failures, 'method': 'fresh omp read skill://<name>; no model invocation'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cwd', type=Path, action='append')
    args = parser.parse_args()
    try:
        rows = [inspect(cwd) for cwd in (args.cwd or [ROOT])]
        print(json.dumps(rows, indent=2))
        return int(any(row['status'] != 'PASS' for row in rows))
    except (OSError, subprocess.TimeoutExpired) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
