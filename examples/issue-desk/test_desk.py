import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

CLI = Path(__file__).with_name('desk.py')
SEED = [
    {'id': 1, 'title': 'Closed investigation', 'status': 'done'},
    {'id': 2, 'title': 'Fix search', 'status': 'open'},
    {'id': 3, 'title': 'Document launch', 'status': 'open'},
    {'id': 4, 'title': 'Old release', 'status': 'done'},
    {'id': 5, 'title': 'Verify handoff', 'status': 'open'},
]


class IssueDeskTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pstack-desk-data-')
        self.addCleanup(self.temp.cleanup)
        self.data = Path(self.temp.name) / 'issues.json'
        self.data.write_text(json.dumps(SEED))

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(CLI), '--data', str(self.data), *args], text=True, capture_output=True, timeout=10)

    def test_filter_then_paginate(self):
        result = self.run_cli('list', '--status', 'open', '--limit', '2')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual([issue['id'] for issue in json.loads(result.stdout)], [2, 3])
        next_page = self.run_cli('list', '--status', 'open', '--limit', '2', '--offset', '2')
        self.assertEqual([issue['id'] for issue in json.loads(next_page.stdout)], [5])

    def test_done_persists_and_disappears_from_open(self):
        self.assertEqual(self.run_cli('done', '2').returncode, 0)
        result = self.run_cli('list', '--status', 'open')
        self.assertEqual([issue['id'] for issue in json.loads(result.stdout)], [3, 5])
        self.assertEqual(json.loads(self.data.read_text())[1]['status'], 'done')

    def test_unknown_issue_does_not_mutate_data(self):
        before = self.data.read_bytes()
        self.assertEqual(self.run_cli('done', '999').returncode, 3)
        self.assertEqual(self.data.read_bytes(), before)

    def test_invalid_pagination_is_rejected(self):
        result = self.run_cli('list', '--offset', '-1')
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(self.data.read_text()), SEED)


if __name__ == '__main__':
    unittest.main()
