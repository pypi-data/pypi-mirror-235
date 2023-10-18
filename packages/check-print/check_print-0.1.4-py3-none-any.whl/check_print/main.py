import argparse
import re
from typing import Sequence

RE_PATTERN = re.compile(b'((def)\s+|([\W])\s*)(print\s*\()')
RE_PATTERN_BEGIN = re.compile(b'^print\s*\(')

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    retcode = 0
    for filename in args.filenames:
        if not filename.endswith('.py'):
            continue
        
        context = ''
        with open(filename, 'rb') as inputfile:
            context = inputfile.read()

            search = RE_PATTERN_BEGIN.finditer(context)
            for matchNum, match in enumerate(search, start=1):
                retcode = 1
                inputfile.seek(0)
                lines_count = inputfile.read(match.end()).count(b'\n') + 1
                print(f'{filename}:{lines_count}: print found')

            search = RE_PATTERN.finditer(context)
            for matchNum, match in enumerate(search, start=1):
                inputfile.seek(0)
                lines_number = inputfile.read(match.end()).count(b'\n') + 1
                if match.group(3) == b'.' or match.group(2) == b'def':
                    continue
                retcode = 1
                print(f'{filename}:{lines_number}: print found')

    return retcode


if __name__ == '__main__':
    raise SystemExit(main())
