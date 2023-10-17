from __future__ import annotations

import argparse
import re
from typing import Sequence

RE_PATTERN = re.compile(b'[\bprint\s*\(')


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        if not filename.endswith('.py'):
            continue

        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile, start=1):
                if RE_PATTERN.search(line):
                    print(
                        f'{filename}:{i}: print found',
                    )
                    retcode = 1

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
