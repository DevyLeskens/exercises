import argparse

parser = argparse.ArgumentParser(prog='range')
parser.add_argument('start', type=int, help='Geef een startnummer.')
parser.add_argument('end', type=int, help='Geef een eindnummer.')
parser.add_argument('-x', action='store_const', const=0, dest='end_delta')
parser.add_argument('--step', default=1, type=int)
parser.set_defaults(end_delta=1)

args = parser.parse_args()

start = args.start
end = args.end + args.end_delta
step = args.step

for i in range(start, end, step):
    print(i)
