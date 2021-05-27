import argparse

parser = argparse.ArgumentParser(prog='find')
parser.add_argument('--minimum-size', default=0, type=int,
                    help="Only files whose size is at least N must be listed.")
parser.add_argument('--maximum-size', default=float('inf'), type=int,
                    help="Only files whose size is at least N must be listed.")
