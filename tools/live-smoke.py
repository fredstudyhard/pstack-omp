#!/usr/bin/env python3
"""Run one finite synthetic OMP journey, retaining no raw reasoning or transcripts."""
import argparse
import json
import os
import signal
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def clean(text, cwd):
    return str(text).replace(str(cwd), '$WORKSPACE').replace(str(Path.home()), '~')


def run_bounded(command, cwd, timeout):
    with subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                          text=True, start_new_session=True) as process:
        try:
            stdout, stderr = process.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.communicate()
            raise
        return subprocess.CompletedProcess(command, process.returncode, stdout, stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cwd', type=Path, required=True)
    parser.add_argument('--name', required=True)
    parser.add_argument('--seconds', type=int, default=300)
    parser.add_argument('--prompt-file', type=Path, required=True)
    parser.add_argument('--model', help='optional explicit host model selector; otherwise preserve OMP defaults')
    args = parser.parse_args()
    if args.seconds < 1 or args.seconds > 600:
        parser.error('seconds must be in 1..600')
    cwd = args.cwd.resolve()
    output = ROOT / '.audit/pstack/live' / (args.name + '.json')
    if not args.name.replace('-', '').isalnum():
        parser.error('name must contain only letters, digits and hyphens')
    prompt = args.prompt_file.read_text()
    command = ['omp', '--mode', 'json', '--no-session', '--no-title', '--no-extensions', '--no-lsp',
               '--max-time', str(args.seconds), '--config', str(ROOT / 'examples/smoke.yml')]
    if args.model:
        command += ['--model', args.model]
    command += ['-p', prompt]
    started = time.monotonic()
    try:
        result = run_bounded(command, cwd, args.seconds + 30)
    except subprocess.TimeoutExpired:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps({'name': args.name, 'status': 'TIMEOUT', 'deadline_seconds': args.seconds}, indent=2) + '\n')
        print(output)
        return 1
    summaries = []
    reads = []
    tools = []
    models = set()
    usage = []
    errors = []
    final = ''
    for line in result.stdout.splitlines():
        try:
            event = json.loads(line)
        except ValueError:
            continue
        kind = event.get('type')
        if kind == 'tool_execution_start':
            name = event.get('toolName', '')
            tools.append(name)
            fields = event.get('args', {})
            if isinstance(fields, dict):
                path = fields.get('path')
                if name == 'read' and isinstance(path, str):
                    reads.append(clean(path, cwd))
                if name == 'bash' and isinstance(fields.get('command'), str):
                    summaries.append({'tool': name, 'command': clean(fields['command'][:1000], cwd)})
        if kind == 'tool_execution_end' and event.get('isError'):
            errors.append({'tool': event.get('toolName'), 'error': 'tool returned isError; see bounded final report'})
        if kind == 'message_end':
            message = event.get('message', {})
            if message.get('role') == 'assistant':
                if message.get('model'):
                    models.add(str(message['model']))
                if message.get('usage'):
                    usage.append(message['usage'])
                text = ''.join(part.get('text', '') for part in message.get('content', []) if part.get('type') == 'text')
                if text:
                    final = clean(text, cwd)
        if kind in ('error', 'notice'):
            errors.append({'event': kind, 'message': clean(event.get('message', ''), cwd)[:1000]})
    record = {'name': args.name, 'process_exit': result.returncode, 'elapsed_seconds': round(time.monotonic() - started, 2), 'models': sorted(models), 'tools': tools, 'reads': reads, 'commands': summaries, 'tool_errors': errors, 'final': final, 'usage': usage, 'stderr': clean(result.stderr, cwd)[-3000:], 'scope': 'synthetic local journey; raw JSONL and reasoning not persisted', 'semantic_status': 'PARENT_VERIFICATION_REQUIRED'}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({key: record[key] for key in ('name', 'process_exit', 'elapsed_seconds', 'models', 'tools', 'reads', 'final', 'stderr')}, indent=2))
    print(f'Evidence: {output}')
    return result.returncode or int(not final)


if __name__ == '__main__':
    raise SystemExit(main())
