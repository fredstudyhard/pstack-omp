import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('omp_install', ROOT / 'tools/omp.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='pstack-install-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / 'repo'
        self.target = self.base / 'native-skills'
        self.add_source('alpha')
        self.add_source('beta')

    def add_source(self, name):
        directory = self.repo / 'skills' / name
        directory.mkdir(parents=True)
        (directory / 'SKILL.md').write_text(f'---\nname: pstack-{name}\ndescription: Native behavior\n---\nRun the native behavior.\n')
        (directory / 'reference.md').write_text('Original reference\n')

    def test_collision_is_detected_before_any_install_write(self):
        collision = self.target / 'pstack-beta'
        collision.mkdir(parents=True)
        (collision / 'SKILL.md').write_text('user-owned\n')
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertFalse((self.target / 'pstack-alpha').exists())
        self.assertEqual((collision / 'SKILL.md').read_text(), 'user-owned\n')

    def test_dry_run_does_not_create_root(self):
        self.assertEqual(installer.install(self.target, self.repo, dry_run=True)['status'], 'DRY_RUN')
        self.assertFalse(self.target.exists())

    def test_disable_and_update_preserve_unrelated_files_without_deletion(self):
        installer.install(self.target, self.repo)
        unrelated = self.target / 'personal.txt'
        unrelated.write_text('keep me\n')
        before = sorted(str(p.relative_to(self.target)) for p in self.target.rglob('*'))
        self.assertEqual(installer.disable(self.target, self.repo)['deleted'], 0)
        for name in ('alpha', 'beta'):
            self.assertEqual(installer.frontmatter((self.target / f'pstack-{name}/SKILL.md').read_text())['enabled'], 'false')
        self.assertEqual(sorted(str(p.relative_to(self.target)) for p in self.target.rglob('*')), before)
        (self.repo / 'skills/alpha/reference.md').write_text('Updated reference\n')
        installer.install(self.target, self.repo)
        self.assertEqual((self.target / 'pstack-alpha/reference.md').read_text(), 'Updated reference\n')
        self.assertNotIn('enabled', installer.frontmatter((self.target / 'pstack-alpha/SKILL.md').read_text()))
        self.assertEqual(unrelated.read_text(), 'keep me\n')

    def test_local_edit_prevents_update_and_is_not_overwritten(self):
        installer.install(self.target, self.repo)
        changed = self.target / 'pstack-beta/reference.md'
        changed.write_text('local fix\n')
        (self.repo / 'skills/alpha/reference.md').write_text('upstream change\n')
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertEqual(changed.read_text(), 'local fix\n')
        self.assertEqual((self.target / 'pstack-alpha/reference.md').read_text(), 'Original reference\n')

    def test_installed_symlink_cannot_redirect_an_update(self):
        installer.install(self.target, self.repo)
        outside = self.base / 'outside.txt'
        outside.write_text('private owner\n')
        entry = self.target / 'pstack-alpha/reference.md'
        entry.unlink()
        entry.symlink_to(outside)
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertEqual(outside.read_text(), 'private owner\n')

    def test_symlink_entrypoint_cannot_redirect_disable(self):
        installer.install(self.target, self.repo)
        outside = self.base / 'outside.txt'
        outside.write_text('private owner\n')
        entry = self.target / 'pstack-alpha/SKILL.md'
        entry.unlink()
        entry.symlink_to(outside)
        with self.assertRaises(ValueError):
            installer.disable(self.target, self.repo)
        self.assertEqual(outside.read_text(), 'private owner\n')

    def test_marker_path_traversal_is_rejected_before_read_or_write(self):
        installer.install(self.target, self.repo)
        marker = self.target / 'pstack-alpha' / installer.MARKER
        metadata = json.loads(marker.read_text())
        metadata['files']['../../outside.txt'] = 'untrusted'
        marker.write_text(json.dumps(metadata))
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertFalse((self.base / 'outside.txt').exists())

    def test_source_symlink_rejected_before_install(self):
        (self.repo / 'skills/beta/link.md').symlink_to(self.repo / 'skills/alpha/reference.md')
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertFalse(self.target.exists())

    def test_ancestor_symlink_rejected_for_fresh_install_and_disable(self):
        outside = self.base / 'outside'
        outside.mkdir()
        redirect = self.base / 'redirect'
        redirect.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(redirect / 'native-skills', self.repo)
        self.assertFalse((outside / 'native-skills').exists())
        installer.install(outside / 'native-skills', self.repo)
        before = (outside / 'native-skills/pstack-alpha/SKILL.md').read_bytes()
        with self.assertRaises(ValueError):
            installer.disable(redirect / 'native-skills', self.repo)
        self.assertEqual((outside / 'native-skills/pstack-alpha/SKILL.md').read_bytes(), before)

    def test_hardlinked_installed_file_cannot_overwrite_external_alias(self):
        installer.install(self.target, self.repo)
        installed = self.target / 'pstack-alpha/reference.md'
        outside = self.base / 'external-reference.md'
        os.link(installed, outside)
        (self.repo / 'skills/alpha/reference.md').write_text('New upstream content\n')
        with self.assertRaises(ValueError):
            installer.install(self.target, self.repo)
        self.assertEqual(outside.read_text(), 'Original reference\n')

    def test_hardlinked_entrypoint_and_marker_cannot_be_mutated_by_disable(self):
        installer.install(self.target, self.repo)
        for relative in ('SKILL.md', installer.MARKER):
            with self.subTest(relative=relative):
                installed = self.target / 'pstack-alpha' / relative
                outside = self.base / ('external-' + relative)
                os.link(installed, outside)
                before = outside.read_bytes()
                with self.assertRaises(ValueError):
                    installer.disable(self.target, self.repo)
                self.assertEqual(outside.read_bytes(), before)
                outside.unlink()


if __name__ == '__main__':
    unittest.main()
