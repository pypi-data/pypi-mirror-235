import os
import re
import subprocess
import sys
import uuid
from pathlib import Path

from textual.message import Message
from textual.widgets import DataTable
from textual.widgets.data_table import RowKey

from . import ICONS
from .text_plus import TextPlus


class PathRow:
    class PathRenamed(Message):
        """Sent when a row (path) is renamed."""

        def __init__(self, path: Path, row_key: RowKey, previous_path: Path) -> None:
            self.path = path
            self.row_key = row_key
            self.previous_path = previous_path
            super().__init__()

    def __init__(self, path: Path, parent: DataTable) -> None:  # type: ignore[type-arg]
        self.path = path if path.is_absolute() else path.absolute()
        self.parent = parent
        self.app = parent.app
        self.row_key: RowKey = RowKey(str(uuid.uuid4()))
        self._new_name: str = self.path.name
        self._new_path: Path = self.path

    @property
    def row_info(self) -> tuple[str, str, TextPlus]:
        return (self.icon, self.path.name, self.new_name_pretty)

    @property
    def icon(self) -> str:
        return self.overwrite_alert if self.overwrite_alert else self.kind

    @property
    def kind(self) -> str:
        return ICONS["folder"] if self.path.is_dir() else ICONS["file"]

    @property
    def new_name(self) -> str:
        return self._new_name

    @new_name.setter
    def new_name(self, value: str) -> None:
        if value == self.new_name:
            return
        self._new_name = value if value else self.path.name
        self.update_row()

    @property
    def new_name_pretty(self) -> TextPlus:
        return (
            TextPlus(self.path.name, style="dim")
            if self.new_name == self.path.name
            else TextPlus(self.new_name, style="bold")
        )

    @property
    def new_path(self) -> Path:
        return self.path.parent.joinpath(self.new_name)

    def reset(self) -> None:
        self.new_name = self.path.name
        self.update_row()

    def apply_substitution(
        self,
        find: re.Pattern[str],
        replace: str,
        first_match: bool,
        ignore_extension: bool,
    ) -> None:
        """Apply regex substitution to the current path name.

        Args:
            find: Regular expression pattern to use for matching.
            replace: Regular expression pattern to use for substitution.
            first_match: Regular expression will only match the first occurrence.
            ignore_extension: Ignore path extension (if applicable)
            when applying regex substitution.
        """

        """Apply regex substitution to the current path name.

        Args:
            find: Regular expression pattern to use for matching.
            replace: Regular expression pattern to use for substitution.
            first_match: Regular expression will only match the first occurrence.
        """
        current_name = (
            self.path.stem
            if ignore_extension and not self.path.is_dir()
            else self.path.name
        )
        name_after_substitution = find.sub(
            replace, current_name, 1 if first_match else 0
        )
        self.new_name = (
            name_after_substitution + self.path.suffix
            if ignore_extension and not self.path.is_dir()
            else name_after_substitution
        )

    def update_row(self) -> None:
        """Update a table tow with new information."""
        self.parent.call_after_refresh(
            self.parent.update_cell,
            self.row_key,
            "icon",
            self.icon,
            update_width=True,
        )
        self.parent.call_after_refresh(
            self.parent.update_cell,
            self.row_key,
            "current_name",
            self.path.name,
            update_width=True,
        )
        self.parent.call_after_refresh(
            self.parent.update_cell,
            self.row_key,
            "new_name",
            self.new_name_pretty,
            update_width=True,
        )

    @property
    def overwrite_alert(self) -> str:
        if self.new_path.exists() and self.path.name.lower() != self.new_name.lower():
            return ICONS["alert"]
        return ""

    def rename(self) -> None:
        previous_path = self.path
        self.path = self.path.replace(self.new_path)
        self.new_name = self.path.name
        self.update_row()
        self.app.post_message(self.PathRenamed(self.path, self.row_key, previous_path))

    def reveal_path(self) -> None:
        """Reveal a path on the system."""
        platform = sys.platform
        if platform == "win32":
            opener = "os.startfile"
            os.startfile(self.path)  # type: ignore
        else:
            opener = "open" if platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.path])

    def __eq__(self, other: object) -> bool:
        """Returns True if both instances have the same path."""
        if not isinstance(other, PathRow):
            return False
        return self.path == other.path
