#!/usr/bin/env python3
"""Resolve primary skills and internal guides through fresh model-free OMP readers."""
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

from omp import ROOT, PRIMARY_SKILLS, inventory, installed_path


def inspect(cwd):
    entries = inventory()
    agent_root = Path(os.environ.get('PI_CODING_AGENT_DIR', str(Path.home() / '.omp/agent')))
    target = agent_root / 'skills'
    primary = []
    internal = []
    failures = []
    for name, source in entries:
        relative = installed_path(source / 'SKILL.md', ROOT)
        if name in PRIMARY_SKILLS:
            uri = 'skill://' + name
        else:
            uri = 'skill://pstack-poteto-mode/' + relative.relative_to('pstack-poteto-mode').as_posix()
        result = subprocess.run(['omp', 'read', uri], cwd=cwd, capture_output=True, text=True, timeout=20)
        text = result.stdout + result.stderr
        match = re.search(r'\[Skill file: ([^\n]+)\]', text)
        if result.returncode != 0:
            failures.append({'name': name, 'uri': uri, 'error': text.splitlines()[0] if text else f'exit {result.returncode}'})
        elif not match or Path(match[1]) != target / relative:
            failures.append({'name': name, 'uri': uri, 'error': 'resolved source identity mismatch'})
        else:
            (primary if name in PRIMARY_SKILLS else internal).append(name)
    for name in sorted({name for name, _ in entries} - PRIMARY_SKILLS):
        result = subprocess.run(['omp', 'read', 'skill://' + name], cwd=cwd, capture_output=True, text=True, timeout=20)
        if result.returncode == 0 or 'Unknown skill:' not in result.stdout + result.stderr:
            failures.append({'name': name, 'error': 'internal guide still exposed as global skill or reader failed unexpectedly'})
    return {'cwd': str(Path(cwd).resolve()), 'status': 'PASS' if not failures else 'FAIL',
            'primary': primary, 'internal': internal, 'failures': failures,
            'method': 'fresh native reader; exact source identity; internal registry names unavailable; no model prompt'}


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
