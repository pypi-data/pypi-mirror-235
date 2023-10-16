from textual.app import ComposeResult
from textual.containers import Grid
from textual.screen import ModalScreen
from textual.widgets import Button, Label


class DisableOverwriteProtectionModal(ModalScreen[bool]):  # type: ignore
    """Modal dialog `Screen` to confirm disabling path overwrite protection."""

    def compose(self) -> ComposeResult:
        yield Grid(
            Label(
                "Disable Overwrite Protection",
                id="title",
            ),
            Label(
                "Are you sure you want to disable path overwrite protection?",
                id="question",
            ),
            Button("Disable", variant="error", id="disable"),
            Button("Cancel", variant="primary", id="no"),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "disable")
