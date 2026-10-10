"""Command-line entry point: `python -m myproject` or `myproject`."""

import argparse

from myproject import __version__, greet


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="myproject", description=__doc__)
    parser.add_argument("name", nargs="?", default="world", help="who to greet")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
