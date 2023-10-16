import argparse
from sisplit.sisplit import split


def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--jumps', '-j', nargs=1, type=int, required=False, default=[2],
                        help="Number of jumps in file")
    parser.add_argument('path', type=str, nargs=1, help='TIFF file to split')
    args = parser.parse_args()

    split(args.path[0], args.jumps[0])


if __name__ == '__main__':
    main()