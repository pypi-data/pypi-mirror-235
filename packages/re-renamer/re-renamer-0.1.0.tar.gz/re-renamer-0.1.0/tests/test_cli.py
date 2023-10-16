import subprocess
import typing
from importlib.metadata import version
from pathlib import Path

from re_renamer import cli


def test_help():
    result = subprocess.run("re-renamer --help", shell=True)
    assert result.returncode == 0


def test_version():
    result = subprocess.check_output("re-renamer --version", shell=True, text=True)
    version_string = f"re-renamer {version('re-renamer')}\n"
    assert result == version_string


def test_no_arg():
    result = subprocess.run("re-renamer", shell=True)
    assert result.returncode == 1


def test_bad_arg():
    result = subprocess.run("re-renamer -z", shell=True)
    assert result.returncode == 2


def test_stdin(tmp_path: Path):
    fpath = tmp_path.joinpath("test.txt")
    fpath.touch()
    with open(fpath, "w") as f:
        f.write("test_file_1.txt\ntest_file_2.txt\n")
    with open(fpath) as f:
        paths = cli.parse_paths(f)
    assert Path("test_file_1.txt") in paths
    assert Path("test_file_2.txt") in paths


def test_arg_parse_simple_args():
    args = cli.parse_args(["test_path1.txt", "-m"])
    assert "test_path1.txt" in args.paths
    assert not args.find and not args.replace
    assert not args.case_sensitive
    assert args.first_match


def test_arg_parse_all_args():
    args = cli.parse_args(["test_path1.txt", "-f foo", "-r bar", "-c", "-m"])
    assert "test_path1.txt" in args.paths
    assert args.find.strip() == "foo"
    assert args.replace.strip() == "bar"
    assert args.case_sensitive and args.first_match


def test_parse_paths_list():
    paths = cli.parse_paths(["test_path1.txt", "test_path2.txt"])
    assert Path("test_path1.txt") in paths and Path("test_path2.txt") in paths


@typing.no_type_check
def test_tui_args():
    app = cli.tui(
        paths=[Path("test_path_1.txt")],
        find="find",
        replace="replace",
        case_sensitive=True,
        first_match=False,
    )
    assert app._paths == [Path("test_path_1.txt")]
    assert app._find == "find"
    assert app._replace == "replace"
    assert app._case_sensitive
    assert not app._first_match
