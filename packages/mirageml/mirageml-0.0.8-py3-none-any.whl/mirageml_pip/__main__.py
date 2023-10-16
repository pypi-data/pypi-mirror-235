import argparse
from .commands import hello, help

def main():
    parser = argparse.ArgumentParser(description="mypackage CLI")
    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser('hello', help='prints hello world')

    args = parser.parse_args()

    if args.command == "hello":
        hello()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
