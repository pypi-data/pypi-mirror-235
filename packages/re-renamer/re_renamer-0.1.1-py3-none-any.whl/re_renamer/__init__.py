__all__ = [
    "__version__",
]


import tempfile
from pathlib import Path


def __getattr__(name: str) -> str:
    """Lazily get the version when needed."""

    if name == "__version__":
        from importlib.metadata import version

        return version("re_renamer")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def is_file_system_case_sensitive() -> bool:
    """Determine if the file system is case sensitive"""
    with tempfile.TemporaryDirectory() as td:
        tmpdir = Path(td)
        p1 = tmpdir.joinpath("abc.txt")
        p1.touch()
        p2 = tmpdir.joinpath("ABC.txt")
        p2.touch()
        return len(list(tmpdir.iterdir())) == 2


ROOT_PATH: Path = Path(__path__[0]).parents[1]
PATH_LOG_FP: Path = ROOT_PATH.joinpath("logs", "path.log")
REGEX_LOG_FP: Path = ROOT_PATH.joinpath("logs", "regex.log")
FILE_SYSTEM_CASE_SENSITIVE: bool = is_file_system_case_sensitive()

ICONS: dict[str, str] = {
    "alert": "⚠️ ",
    "check": "✅",
    "file": "📄",
    "folder": "📁",
    "info": "ℹ️ ",
    "trash": "🗑️ ",
    "warning": "🚨",
}
