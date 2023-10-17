import sys
from argparse import ArgumentParser, Namespace
from collections.abc import Sequence
from importlib.metadata import version
from io import TextIOWrapper
from pathlib import Path

from textual.app import App


def parse_args(argv: Sequence[str] | None = None) -> Namespace:
    parser = ArgumentParser(
        description="[RE]name FILES and DIRECTORIES using [RE]gex.",
        epilog="Copyright 2023 Josh Duncan (joshbduncan.com)",
    )
    parser.add_argument(
        "paths",
        type=str,
        nargs="*",
        default=sys.stdin,
        help="paths to rename",
    )
    parser.add_argument(
        "-f",
        "--find",
        type=str,
        default="",
        help="Regular expression search string.",
    )
    parser.add_argument(
        "-r",
        "--replace",
        type=str,
        default="",
        help="Regular expression substitution string.",
    )
    parser.add_argument(
        "-c",
        "--case-sensitive",
        action="store_true",
        help="Enable case-sensitive querying.",
    )
    parser.add_argument(
        "-m",
        "--first-match",
        action="store_true",
        help="Query will only match the first occurrence.",
    )
    parser.add_argument(
        "-x",
        "--ignore-extension",
        action="store_true",
        help="Query will ignore file extensions.",
    )
    parser.add_argument(
        "-d",
        "--disable-protection",
        action="store_true",
        help="Disable path overwrite protection.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {version('re_renamer')}",
    )
    return parser.parse_args(argv)


def parse_paths(paths: list[str] | TextIOWrapper) -> list[Path]:
    if isinstance(paths, list):
        return sorted([Path(path) for path in paths])
    elif not sys.stdin.isatty():
        # disable interactive tty which can be confusing
        # but still process info piped in from the shell
        return sorted([Path(path.strip()) for path in paths.readlines()])
    return []


def tui(*args, **kwargs) -> App[int]:
    from re_renamer.app import REnamer

    app = REnamer(*args, **kwargs)
    return app


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    paths = parse_paths(args.paths)

    if not paths:
        print("No paths provided. Learn more with the '-h' flag.", file=sys.stderr)
        return 1

    app = tui(
        paths=paths,
        find=args.find,
        replace=args.replace,
        case_sensitive=args.case_sensitive,
        first_match=args.first_match,
        ignore_extension=args.ignore_extension,
        overwrite_protection=not args.disable_protection,
    )
    return app.run()  # type: ignore[return-value, no-any-return]


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
