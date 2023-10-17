import os
import re
import subprocess
import sys
from pathlib import Path
from typing import TYPE_CHECKING, Iterable

from rich.text import Text
from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.events import Mount, Ready
from textual.reactive import reactive
from textual.widgets import Button, Checkbox, Footer, Header, Input

from . import FILE_SYSTEM_CASE_SENSITIVE, PATH_LOG_FP
from .logging import path_logger, regex_logger
from .path_row import PathRow
from .screens.disable_overwrite_protection_modal import DisableOverwriteProtectionModal
from .widgets import Buttons, Inputs, Log, Options, Table
from .widgets.inputs import InputWithHistory

if TYPE_CHECKING:
    from textual.widgets.data_table import RowKey


class REnamer(App[int]):
    """TUI renaming app."""

    TITLE = "[RE]namer"
    CSS_PATH = Path(__file__).parent.joinpath("style.tcss")
    BINDINGS = [
        Binding("ctrl+c", "exit_app", "Quit", show=True),
        Binding("ctrl+l", "show_log", "Show Log", show=True),
    ]

    find: reactive[str] = reactive("", init=False, always_update=False)
    replace: reactive[str] = reactive("", init=False, always_update=False)
    case_sensitive: reactive[bool] = reactive(False, init=False, always_update=False)
    first_match: reactive[bool] = reactive(False, init=False, always_update=False)
    ignore_extension: reactive[bool] = reactive(False, init=False, always_update=False)
    overwrite_protection: reactive[bool] = reactive(True)

    def __init__(
        self,
        paths: Path | Iterable[Path],
        find: str = "",
        replace: str = "",
        case_sensitive: bool = False,
        first_match: bool = False,
        ignore_extension: bool = False,
        overwrite_protection: bool = True,
        *args,
        **kwargs,
    ) -> None:
        """Initialize an instance of the app.

        Args:
            paths: System paths to load.
            find: Regular expression search string. Defaults to "".
            replace: Regular expression substitution string. Defaults to "".
            case_sensitive: Enable case-sensitive querying. Defaults to False.
            first_match: Query will only match the first occurrence. Defaults to False.
            ignore_extension: Query will ignore file extensions. Defaults to False.
            overwrite_protection: Enable path overwrite protection. Defaults to True.
        """
        self._paths = [paths] if isinstance(paths, Path) else paths
        self.paths: dict[RowKey, PathRow] = {}

        self._find = find
        self._replace = replace
        self._case_sensitive = case_sensitive
        self._first_match = first_match
        self._ignore_extension = ignore_extension
        self._overwrite_protection = overwrite_protection

        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Table(show_cursor=True, zebra_stripes=True, id="paths-table")
        yield Options(
            case_sensitive=self._case_sensitive,
            first_match=self._first_match,
            ignore_extension=self._ignore_extension,
        )
        yield Inputs(find=self._find, replace=self._replace)
        yield Buttons()
        yield Log(overwrite_protection=self._overwrite_protection)

    @on(Mount)
    def load_table(self) -> None:
        self.overwrite_protection = self._overwrite_protection
        self.paths = self.query_one(Table).load_paths_in_table(self._paths)

    @on(Ready)
    def focus_input_load_history(self) -> None:
        self.query_one("#find", Input).focus()
        self.query_one(Inputs).load_history()
        table = self.query_one(Table)
        self.log(f"{table.row_count} paths(s) loaded.")
        self.notify(
            f"{table.row_count} path(s) loaded",
            severity="information",
            title="Path Loading Complete",
        )

    # ***** PATH ACTIONS *****

    @on(Button.Pressed, "#rename")
    def rename_paths(self) -> None:
        """Rename paths."""
        table = self.query_one(Table)
        changed_paths: set[Path] = set()
        paths_to_remove: set[RowKey] = set()

        for row in sorted(
            table.ordered_rows, key=lambda r: str(self.paths[r.key].path).lower()
        ):
            row_key = row.key
            path_row = self.paths[row_key]

            # check to make sure path hasn't already been changed
            if (FILE_SYSTEM_CASE_SENSITIVE and path_row.path in changed_paths) or (
                Path(str(path_row.path).lower()) in changed_paths
            ):
                paths_to_remove.add(row_key)
                continue

            # skip rows with no changes
            if path_row.path.name == path_row.new_name:
                continue

            # don't rename if overwrite protection is enabled
            if path_row.overwrite_alert and self.overwrite_protection:
                continue
            previous_path = path_row.path
            path_row.rename()

            if previous_path != path_row.path:
                if FILE_SYSTEM_CASE_SENSITIVE:
                    changed_paths.add(path_row.path)
                else:
                    changed_paths.add(Path(str(path_row.path).lower()))

        if changed_paths:
            regex_logger.info(f"{self.find}\t{self.replace}")
            self.query_one("#find", InputWithHistory).add_history_entry(self.find)
            self.query_one("#replace", InputWithHistory).add_history_entry(self.replace)
            self.notify(
                f"{len(changed_paths)} path(s) changed.", title="Rename Results"
            )
            for row_key in paths_to_remove:
                del self.paths[row_key]
                table.remove_row(row_key)
            self.reset_values()

    @on(Button.Pressed, "#reset")
    def reset_values(self) -> None:
        """Reset app inputs."""
        find = self.query_one("#find", Input)
        replace = self.query_one("#replace", Input)
        case_sensitive = self.query_one("#case-sensitive", Checkbox)
        first_match = self.query_one("#first-match", Checkbox)

        find.value = self.find
        replace.value = self.replace
        case_sensitive.value = self.case_sensitive
        first_match.value = self.first_match
        self.overwrite_protection = True

        find.focus()

    # ***** OPTION ACTIONS *****

    @on(Checkbox.Changed, "#case-sensitive")
    def update_case_sensitive(self, event: Checkbox.Changed) -> None:
        self.case_sensitive = event.control.value

    @on(Checkbox.Changed, "#first-match")
    def update_first_match(self, event: Checkbox.Changed) -> None:
        self.first_match = event.control.value

    @on(Checkbox.Changed, "#ignore-extension")
    def update_ignore_extension(self, event: Checkbox.Changed) -> None:
        self.ignore_extension = event.control.value

    @on(Button.Pressed, "#overwrite-protection")
    def update_overwrite_protection(self) -> None:
        def callback(disable: bool) -> None:
            self.overwrite_protection = not disable

        if self.overwrite_protection:
            self.push_screen(DisableOverwriteProtectionModal(), callback)
        else:
            self.overwrite_protection = True

    # ***** INPUT ACTIONS *****

    @on(Inputs.RegexInputChanged)
    def update_regex_strings(self, message: Inputs.RegexInputChanged) -> None:
        find = message.find
        replace = message.replace
        self.log(f"Updating regex reactive properties. {find=}, {replace=}")
        if not replace:
            self.replace = replace
        self.find = find
        if replace:
            self.replace = replace

    # ***** DATA TABLE ACTIONS *****

    @on(Table.RevealPath)
    def show_path_row_info(self, message: Table.RevealPath) -> None:
        row_key = message.row_key
        path_row = self.paths[row_key]
        path_row.reveal_path()

    @on(PathRow.PathRenamed)
    def path_renamed(self, message: PathRow.PathRenamed) -> None:
        log = self.query_one(Log)
        path_logger.info(f"{message.previous_path}\t{message.path}")
        msg = Text("Success: ", "bold green")
        msg.append(f"'{message.previous_path.name}' renamed to '{message.path.name}'")
        log.write(msg, True)

    @on(Table.RemovePath)
    def remove_path(self, message: Table.RemovePath) -> None:
        """Remove a path from the table."""
        del self.paths[message.row_key]
        if not self.query_one(Table).row_count:
            self.query_one("#rename", Button).disabled = True

    # ***** WATCH ACTIONS *****

    def update_paths(self) -> None:
        table = self.query_one(Table)
        find = re.compile(self.find, flags=0 if self.case_sensitive else re.IGNORECASE)
        self.log(f"Regex: {self.find=}, {self.replace=}")
        for row_key, path_row in self.paths.items():
            if not self.find:
                path_row.reset()
                continue
            if row_key not in table.rows:
                del self.paths[row_key]
            path_row.apply_substitution(
                find,
                self.replace,
                self.first_match,
                self.ignore_extension,
            )

    def watch_find(self) -> None:
        self.update_paths()
        self.query_one("#rename", Button).disabled = not self.find

    def watch_replace(self) -> None:
        self.update_paths()

    def watch_case_sensitive(self) -> None:
        self.update_paths()

    def watch_first_match(self) -> None:
        self.update_paths()

    def watch_ignore_extension(self) -> None:
        self.update_paths()

    def watch_overwrite_protection(self) -> None:
        button = self.query_one("#overwrite-protection", Button)
        button.variant = "success" if self.overwrite_protection else "error"

    # ***** BINDING ACTIONS *****

    def action_exit_app(self) -> None:
        """Exit the app."""
        self.exit()

    def action_show_log(self) -> None:
        """Open the app change log."""
        path = PATH_LOG_FP
        platform = sys.platform
        if platform == "win32":
            os.startfile(path)  # type: ignore[attr-defined]
        else:
            opener = "open" if platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
