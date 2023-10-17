from textual.app import ComposeResult
from textual.containers import Grid
from textual.widgets import Button


class Buttons(Grid):
    """A custom container to encase the main app buttons."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the container."""
        yield Button("Rename", variant="primary", id="rename", disabled=True)
        yield Button("Reset", variant="default", id="reset")
