import argparse
import os
from pathlib import Path
import re


def minimum_size(size):
    def check(filename):
        return os.path.getsize(filename) >= size


parser = argparse.ArgumentParser(prog='find')
parser.add_argument('path', default='.')
parser.add_argument('--minimum-size', dest='minimum_size', default=0, type=int,
                    help="Only files whose size is at least N must be listed.")
parser.add_argument('--maximum-size', dest='maximum_size', default=float('inf'), type=int,
                    help="Only files whose size is at least N must be listed.")
parser.add_argument('--no-directories', dest='no_directories',
                    default=False, action='store_true')
parser.add_argument('--no-files', dest='no_files',
                    default=False, action='store_true')
parser.add_argument('--extension', dest='extension')
parser.add_argument('--contains', dest='contains')

args = parser.parse_args()

path = Path(args.path)
for item in path.glob('.'):
    if not os.path.getsize(item) >= args.minimum_size:
        continue
    if not os.path.getsize(item) <= args.maximum_size:
        continue
    if args.no_directories and os.path.isdir(item):
        continue

    if args.no_files and os.path.isfile(item):
        continue

    if args.extension and not item.suffix == args.extension:
        continue

    if args.contains:
        if not os.path.isfile(item):
            continue

        with open(item, 'r') as file:
            contents = file.read()

            if not re.search(args.contains, contents):
                continue

    print(item)
