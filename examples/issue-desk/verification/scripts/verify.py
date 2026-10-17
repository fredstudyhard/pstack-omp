#!/usr/bin/env python3
"""Drive the real issue desk CLI with disposable synthetic files; retain proof."""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[4] if Path(__file__).resolve().parents[3].name == '.omp' else Path(__file__).resolve().parents[2]
CLI = ROOT / 'desk.py'
SEED = [{'id': 1, 'title': 'Closed investigation', 'status': 'done'}, {'id': 2, 'title': 'Fix search', 'status': 'open'}, {'id': 3, 'title': 'Document launch', 'status': 'open'}, {'id': 4, 'title': 'Old release', 'status': 'done'}, {'id': 5, 'title': 'Verify handoff', 'status': 'open'}]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    if not __debug__:
        raise RuntimeError('Run without Python optimization; verification assertions must remain enabled')
    evidence = ROOT / '.audit/pstack/verification'
    evidence.mkdir(parents=True, exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix='run-', dir=evidence))
    protected = [ROOT / name for name in ('desk.py', 'test_desk.py', 'issues.json')]
    baseline = {p.name: digest(p) for p in protected}
    report = {'started_utc': datetime.now(timezone.utc).isoformat(), 'cwd': str(ROOT), 'python': sys.executable, 'version': sys.version, 'platform': platform.platform(), 'protected_before': baseline, 'cases': [], 'groups': {}, 'limits': ['Local synthetic CLI only; no external service exists.', 'No real data, credentials, network, application/test edits or seed mutations.', 'Malformed JSON and file I/O errors covered; arbitrary JSON schemas and OS permission variants not exhaustively covered.', 'No long-running server, PTY, browser or dependency installation required.']}
    scratch = None
    try:
        with tempfile.TemporaryDirectory(prefix='verify-issue-desk-') as directory:
            scratch = Path(directory)
            data = scratch / 'issues.json'

            def call(label, args, *, target=data, code=0, expected=None, after=None, unchanged=False, raw=False):
                before = target.read_bytes() if target.is_file() else None
                command = [sys.executable, str(CLI)]
                if not raw:
                    command += ['--data', str(target)]
                command += args
                entry = {'case': label, 'command': command, 'before': None if before is None else before.decode()}
                report['cases'].append(entry)
                try:
                    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=10)
                    current = target.read_bytes() if target.is_file() else None
                    entry.update(stdout=result.stdout, stderr=result.stderr, exit_code=result.returncode, after=None if current is None else current.decode(), target_exists=target.exists(), target_is_file=target.is_file())
                    assert result.returncode == code, entry
                    if expected is not None:
                        assert json.loads(result.stdout) == expected, entry
                    if code == 0:
                        assert result.stderr == '', entry
                    else:
                        assert result.stdout == ''
                    if after is not None:
                        assert json.loads(current) == after, entry
                    if unchanged:
                        assert current == before, entry
                    entry['status'] = 'PASS'
                    print(f'PASS {label}: exit={result.returncode} stdout={result.stdout.strip()!r} stderr={result.stderr.strip()!r}')
                except Exception as exc:
                    entry['status'] = 'FAIL'
                    entry['failure'] = str(exc)
                    raise
            call('doctor-help', ['--help'], raw=True, unchanged=True)
            assert '{list,add,done}' in report['cases'][-1]['stdout']
            call('doctor-empty', ['list'], expected=[], unchanged=True)
            assert not data.exists()
            first = {'id': 1, 'title': 'First synthetic issue', 'status': 'open'}
            call('empty-add', ['add', '  First synthetic issue  '], expected=first, after=[first])
            call('empty-reopen', ['list'], expected=[first], unchanged=True)
            data.write_text(json.dumps(SEED, indent=2) + '\n')
            call('list-all', ['list'], expected=SEED, unchanged=True)
            call('list-open-page-1', ['list', '--status', 'open', '--limit', '2'], expected=[SEED[1], SEED[2]], unchanged=True)
            call('list-open-page-2', ['list', '--status', 'open', '--limit', '2', '--offset', '2'], expected=[SEED[4]], unchanged=True)
            call('list-done', ['list', '--status', 'done'], expected=[SEED[0], SEED[3]], unchanged=True)
            call('list-zero', ['list', '--limit', '0'], expected=[], unchanged=True)
            call('list-beyond-end', ['list', '--offset', '99'], expected=[], unchanged=True)
            report['groups']['list-filter-pagination'] = 'PASS'
            added = {'id': 6, 'title': 'Verify durable change', 'status': 'open'}
            state = SEED + [added]
            call('add-persist', ['add', '  Verify durable change  '], expected=added, after=state)
            call('add-reopen', ['list', '--status', 'open'], expected=[SEED[1], SEED[2], SEED[4], added], unchanged=True)
            completed = dict(added, status='done')
            state = SEED + [completed]
            call('done-persist', ['done', '6'], expected=completed, after=state)
            call('done-open-view', ['list', '--status', 'open'], expected=[SEED[1], SEED[2], SEED[4]], unchanged=True)
            call('done-closed-view', ['list', '--status', 'done'], expected=[SEED[0], SEED[3], completed], unchanged=True)
            call('done-repeat', ['done', '6'], expected=completed, after=state, unchanged=True)
            report['groups']['add-done-persistence'] = 'PASS'
            for (label, args, code) in [('unknown-id', ['done', '999'], 3), ('blank-title', ['add', '   '], 2), ('negative-limit', ['list', '--limit', '-1'], 2), ('negative-offset', ['list', '--offset', '-1'], 2), ('invalid-status', ['list', '--status', 'closed'], 2), ('invalid-id', ['done', 'not-an-integer'], 2), ('missing-title', ['add'], 2), ('missing-action', [], 2), ('unknown-action', ['remove'], 2)]:
                call(label, args, code=code, unchanged=True)
            broken = scratch / 'malformed.json'
            broken.write_text('{not json\n')
            call('malformed-json', ['list'], target=broken, code=2, unchanged=True)
            missing_parent = scratch / 'absent' / 'issues.json'
            call('missing-parent-write', ['add', 'Cannot persist'], target=missing_parent, code=2, unchanged=True)
            assert not missing_parent.parent.exists()
            call('directory-data', ['list'], target=scratch, code=2, unchanged=True)
            report['groups']['refusal-errors'] = 'PASS'
    except Exception as exc:
        report['failure'] = str(exc)
    finally:
        report['scratch_path'] = str(scratch)
        report['scratch_removed'] = scratch is not None and (not scratch.exists())
        report['protected_after'] = {p.name: digest(p) for p in protected}
        report['protected_unchanged'] = baseline == report['protected_after']
        passed = not report.get('failure') and report['scratch_removed'] and report['protected_unchanged'] and (len(report['groups']) == 3)
        report['status'] = 'PASS' if passed else 'FAIL'
        (run / 'report.json').write_text(json.dumps(report, indent=2) + '\n')
        summary = '\n'.join(['# Issue desk verification', '', f"Status: {report['status']}", f"CLI calls: {len(report['cases'])}", f"Groups: {json.dumps(report['groups'], sort_keys=True)}", f"Scratch removed: {report['scratch_removed']}", f"Application, tests and seed unchanged: {report['protected_unchanged']}", 'Detailed commands, stdout/stderr, exit codes and before/after file contents: report.json', *report['limits'], ''])
        (run / 'summary.md').write_text(summary)
        print(summary)
        print(f'Evidence: {run}')
    return 0 if passed else 1
if __name__ == '__main__':
    raise SystemExit(main())
