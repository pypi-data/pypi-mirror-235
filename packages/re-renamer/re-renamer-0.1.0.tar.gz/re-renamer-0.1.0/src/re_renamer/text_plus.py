from rich.text import Text


class TextPlus(Text):
    """Custom patch for a Rich `Text` object to allow Textual `DataTable`
    sorting when a Text object is included in a row."""

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Text):
            return NotImplemented
        return self.plain < other.plain  # type: ignore[no-any-return]

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Text):
            return NotImplemented
        return self.plain <= other.plain  # type: ignore[no-any-return]

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Text):
            return NotImplemented
        return self.plain > other.plain  # type: ignore[no-any-return]

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Text):
            return NotImplemented
        return self.plain >= other.plain  # type: ignore[no-any-return]
