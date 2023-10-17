import re

from textual import on
from textual.app import ComposeResult
from textual.containers import Grid
from textual.events import Blur, Focus, Key
from textual.message import Message
from textual.validation import ValidationResult, Validator
from textual.widgets import Input, Static

from .. import REGEX_LOG_FP


class ValidFindRegex(Validator):
    """Custom regular expression validator."""

    def validate(self, value: str) -> ValidationResult:
        """Check if `value` is a valid regular expression."""
        try:
            re.compile(value)
            print(f"Valid FIND regex. {value=}")
            return self.success()
        except re.error as e:
            print(f"Invalid FIND regex. {value=}, {e.msg=}")
            return self.failure(e.msg)


class ValidSubstitutionRegex(Validator):
    """Custom regular expression substitution validator."""

    def validate(self, value: str, find: str) -> ValidationResult:  # type: ignore
        """Check if `value` is a valid regular expression substitution."""
        try:
            regex = re.compile(find)
            regex.sub(value, "")
            print(f"Valid REPLACE regex. {value=}")
            return self.success()
        except (re.error, IndexError) as e:
            err = e.msg if hasattr(e, "msg") else str(e)
            print(f"Invalid REPLACE regex. {value=}, {err=}")
            return self.failure(err)


class Inputs(Grid):
    """A custom container for Find and Replace inputs."""

    def __init__(self, find: str, replace: str, *args, **kwargs) -> None:
        self._find = find
        self._replace = replace
        super().__init__(*args, **kwargs)

    class RegexInputChanged(Message):
        """Sent when either FIND or REPLACE inputs are changed."""

        def __init__(self, find: str, replace: str) -> None:
            self.find = find
            self.replace = replace
            super().__init__()

    def compose(self) -> ComposeResult:
        """Create child widgets for the container."""
        yield InputWithHistory(value=self._find, placeholder="Find", id="find")
        yield InputWithHistory(value=self._replace, placeholder="Replace", id="replace")
        yield Static(id="find-error")
        yield Static(id="replace-error")

    def load_history(self) -> None:
        """Load previous regular expression history into corresponding input."""
        find = self.query_one("#find", InputWithHistory)
        replace = self.query_one("#replace", InputWithHistory)
        with open(REGEX_LOG_FP) as f:
            for line in f.readlines():
                _, find_str, replace_str = line.strip("\n").split("\t")
                find.add_history_entry(find_str)
                replace.add_history_entry(replace_str)

    @on(Input.Changed)
    def validate_regex_input(self) -> None:
        """Custom input validation, where both Find and Replace inputs
        are validated on a change to either."""
        find = self.query_one("#find", Input)
        find_validation = ValidFindRegex().validate(find.value)
        self.query_one("#find-error", Static).update(
            find_validation.failure_descriptions[-1]
            if not find_validation.is_valid
            else ""
        )
        find.set_class(not find_validation.is_valid, "-invalid")
        find.set_class(find_validation.is_valid, "-valid")

        replace = self.query_one("#replace", Input)
        replace_validation = ValidSubstitutionRegex().validate(
            replace.value, find.value if find_validation.is_valid else ""
        )
        self.query_one("#replace-error", Static).update(
            replace_validation.failure_descriptions[-1]
            if not replace_validation.is_valid
            else ""
        )
        replace.set_class(not replace_validation.is_valid, "-invalid")
        replace.set_class(replace_validation.is_valid, "-valid")

        self.post_message(
            self.RegexInputChanged(
                find.value if find_validation.is_valid else "",
                replace.value if replace_validation.is_valid else "",
            )
        )


class InputWithHistory(Input):
    """A custom `Input` widget with access to history via the up and down arrow keys."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the widget."""
        self.history: list[str] = []
        self.history_idx: int = 0
        self.placeholder_default: str = kwargs.get("placeholder", "")
        super().__init__(*args, **kwargs)

    @on(Focus)
    def update_placeholder_focus(self) -> None:
        """Update input placeholder information on focus."""
        if self.history:
            self.placeholder += " (↑↓ for history)"  # type: ignore[has-type]

    @on(Blur)
    def update_placeholder_blur(self) -> None:
        """Update input placeholder information on blur."""
        if self.placeholder != self.placeholder_default:  # type: ignore[has-type]
            self.placeholder = self.placeholder_default

    @on(Key)
    def iterate_through_history(self, event: Key) -> None:
        """Iterate through the input history depending on the `event.Key`."""
        if event.key not in ["up", "down"]:
            self.history_idx = 0
            return
        self.history_idx = self.calculate_history_idx(event.key)
        if self.history_idx:
            self.value = self.history[-self.history_idx] if self.history_idx else ""
            self.cursor_position = len(self.value)
            return
        self.value = ""

    def add_history_entry(self, value: str) -> None:
        """Add an event to the input history."""
        if value in self.history:
            self.history.remove(value)
        self.history.append(value)

    def calculate_history_idx(self, direction: str) -> int:
        """Determine the current history based user input (directional key).

        Args:
            direction: The direction to move through the index (up or down).

        Returns:
            Calculated history index.
        """
        if direction == "up":
            if self.history_idx == len(self.history):
                return self.history_idx
            return self.history_idx + 1
        else:
            if self.history_idx <= 1:
                return 0
            return self.history_idx - 1
