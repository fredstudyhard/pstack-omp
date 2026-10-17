import { test, expect } from 'bun:test';
import { spawnSync } from 'node:child_process';
import { copyFileSync, mkdtempSync, realpathSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { fileURLToPath } from 'node:url';

const bootstrap = fileURLToPath(new URL('../skills/poteto-mode/scripts/bootstrap.ts', import.meta.url));

test('missing helper dependencies fail without launching any installer or network subprocess', () => {
  const root = realpathSync(mkdtempSync(join(tmpdir(), 'pstack-bootstrap-')));
  try {
    copyFileSync(bootstrap, join(root, 'bootstrap.ts'));
    writeFileSync(join(root, 'package.json'), JSON.stringify({ dependencies: { commander: '14.0.0' } }));
    writeFileSync(join(root, 'run.mjs'), `
import { ensureDependenciesInstalled } from './bootstrap.ts';
const attempts = [];
Bun.spawnSync = (...args) => { attempts.push(args); throw new Error('unexpected process'); };
let missing = false;
try { ensureDependenciesInstalled(); } catch (error) { missing = error.message.includes('Missing reviewed pstack helper dependency'); }
console.log(JSON.stringify({ missing, attempts }));
`);
    const result = spawnSync(process.execPath, [join(root, 'run.mjs')], { encoding: 'utf8', timeout: 5000 });
    expect(result.status).toBe(0);
    expect(JSON.parse(result.stdout)).toEqual({ missing: true, attempts: [] });
  } finally {
    rmSync(root, { recursive: true, force: true });
  }
});
