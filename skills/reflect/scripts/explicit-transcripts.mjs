import { statSync } from 'node:fs';

export function rethrowUnlessRemoved(error) {
  if (error.code !== 'ENOENT') throw error;
}

export function candidates(path) {
  const stat = statSync(path, { throwIfNoEntry: false });
  if (!stat?.isFile() || !path.endsWith('.jsonl')) {
    throw new Error('Pass one explicitly authorized .jsonl file, not a session directory');
  }
  return [{ path, mtime: stat.mtimeMs }];
}
