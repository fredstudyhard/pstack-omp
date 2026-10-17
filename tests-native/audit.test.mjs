import { test, expect } from 'bun:test';
import { execFileSync, spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, mkdtempSync, readFileSync, realpathSync, rmSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { classify } from '../skills/poteto-mode/scripts/worktree-audit.mjs';
import { candidates } from '../skills/reflect/scripts/explicit-transcripts.mjs';

const script = fileURLToPath(new URL('../skills/poteto-mode/scripts/worktree-audit.mjs', import.meta.url));

test('offline worktree audit never reaches any remote Git transport', () => {
  const root = realpathSync(mkdtempSync(join(tmpdir(), 'pstack-offline-audit-')));
  try {
    const repo = join(root, 'repo');
    const bin = join(root, 'bin');
    mkdirSync(repo);
    mkdirSync(bin);
    execFileSync('/usr/bin/git', ['init', '-b', 'main'], { cwd: repo, stdio: 'pipe' });
    const log = join(root, 'remote-attempts.txt');
    writeFileSync(join(bin, 'git'), '#!/bin/sh\ncase "$*" in *ls-remote*|*fetch*) printf "%s\\n" "$*" >> "$REMOTE_LOG"; exit 77;; esac\nexec /usr/bin/git "$@"\n', { mode: 0o755 });
    const result = spawnSync('node', [script, repo], { encoding: 'utf8', env: { ...process.env, PATH: `${bin}:${process.env.PATH}`, REMOTE_LOG: log }, timeout: 10000 });
    expect(result.status).toBe(0);
    expect(existsSync(log) ? readFileSync(log, 'utf8') : '').toBe('');
    expect(result.stdout.split('\n')[0].split('\t')).toContain('BUCKET');
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

test('history helper accepts a named transcript file and rejects directory discovery', () => {
  const root = realpathSync(mkdtempSync(join(tmpdir(), 'pstack-explicit-history-')));
  try {
    const file = join(root, 'named.jsonl');
    writeFileSync(file, '{"type":"session","version":1,"cwd":"/synthetic"}\n');
    expect(candidates(file).map(row => row.path)).toEqual([file]);
    expect(() => candidates(root)).toThrow();
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});

const known = value => ({ known: true, value });
const clean = () => ({ locked: known(null), dirty: known({ wip: 0, untracked: 0, ignored: 0 }), orphans: known(0), pr: known(null), recent: known(false), ancestry: known(true), head: known('reviewed') });

test('cleanup classification holds untracked data and uncertainty even when merged', () => {
  expect(classify(clean())).toBe('safe');
  const untracked = clean();
  untracked.dirty = known({ wip: 0, untracked: 1, ignored: 0 });
  expect(classify(untracked)).toBe('hold-untracked');
  const uncertain = clean();
  uncertain.recent = { known: false };
  expect(classify(uncertain)).toBe('review');
  const locked = clean();
  locked.locked = known('another owner');
  expect(classify(locked)).toBe('hold-locked');
});
