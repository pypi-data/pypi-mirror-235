import datetime

from rich.text import Text
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Grid
from textual.widgets import Button, RichLog, Static


class OverwriteProtectionStatus(Container):
    """A custom container to encase the app overwrite protection status."""


class Log(Container):
    """A custom container to encase the app activity log."""

    BINDINGS = [
        Binding("ctrl+d", "clear_activity_log", "Clear Activity Log", show=True),
    ]

    def __init__(self, overwrite_protection: bool, *args, **kwargs) -> None:
        self._overwrite_protection = overwrite_protection
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with Grid(id="log-header"):
            yield Static("Activity:")
            yield Button(
                "Overwrite Protection",
                id="overwrite-protection",
                variant="success" if self._overwrite_protection else "error",
            )
        yield RichLog(id="rich-log")

    def write(self, value: Text | str, include_timestamp: bool = False) -> None:
        """Write to the activity log.

        Args:
            value: Information to write.
            include_timestamp: Include a timestamp. Defaults to False.
        """
        text = Text()
        if include_timestamp:
            timestamp = f"[{datetime.datetime.now().strftime('%H:%M:%S')}] "
            text.append(timestamp)
        text.append(value)
        self.query_one("#rich-log", RichLog).write(text)

    def action_clear_activity_log(self) -> None:
        """Clear the log."""
        self.query_one("#rich-log", RichLog).clear()
