#!/usr/bin/env python3
"""A small local issue desk with JSON output and no network dependencies."""
import argparse
import json
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, default=Path('issues.json'))
    actions = parser.add_subparsers(dest='action', required=True)
    listing = actions.add_parser('list')
    listing.add_argument('--status', choices=('open', 'done', 'all'), default='all')
    listing.add_argument('--limit', type=int, default=10)
    listing.add_argument('--offset', type=int, default=0)
    adding = actions.add_parser('add')
    adding.add_argument('title')
    done = actions.add_parser('done')
    done.add_argument('id', type=int)
    args = parser.parse_args()
    try:
        issues = json.loads(args.data.read_text()) if args.data.exists() else []
        if args.action == 'list':
            if args.limit < 0 or args.offset < 0:
                parser.error('limit and offset must be nonnegative')
            selected = [issue for issue in issues if args.status == 'all' or issue['status'] == args.status]
            result = selected[args.offset:args.offset + args.limit]
        elif args.action == 'add':
            if not args.title.strip():
                parser.error('title must not be blank')
            result = {'id': max((issue['id'] for issue in issues), default=0) + 1, 'title': args.title.strip(), 'status': 'open'}
            issues.append(result)
            args.data.write_text(json.dumps(issues, indent=2) + '\n')
        else:
            result = next((issue for issue in issues if issue['id'] == args.id), None)
            if result is None:
                print(f'issue {args.id} does not exist', file=sys.stderr)
                return 3
            result['status'] = 'done'
            args.data.write_text(json.dumps(issues, indent=2) + '\n')
        print(json.dumps(result))
        return 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'cannot use issue data: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
