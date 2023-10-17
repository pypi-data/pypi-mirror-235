from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Checkbox


class Options(Horizontal):
    """A custom container to encase the app option checkboxes."""

    def __init__(
        self,
        case_sensitive: bool,
        first_match: bool,
        ignore_extension: bool,
        *args,
        **kwargs,
    ) -> None:
        self._case_sensitive = case_sensitive
        self._first_match = first_match
        self._ignore_extension = ignore_extension
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield Checkbox(
            "Case Sensitive", value=self._case_sensitive, id="case-sensitive"
        )
        yield Checkbox("First Match Only", value=self._first_match, id="first-match")
        yield Checkbox(
            "Ignore Extension", value=self._ignore_extension, id="ignore-extension"
        )
