from textual import on
from textual.binding import Binding
from textual.events import Mount
from textual.message import Message
from textual.widgets import DataTable
from textual.widgets.data_table import RowKey

from ..path_row import PathRow


class Table(DataTable):  # type: ignore[type-arg]
    """A custom Textual `DataTable`."""

    class RevealPath(Message):
        """Sent when a row (path) icon is clicked."""

        def __init__(self, row_key: RowKey) -> None:
            self.row_key = row_key
            super().__init__()

    class RemovePath(Message):
        """Sent when a row (path) is removed."""

        def __init__(self, row_key: RowKey) -> None:
            self.row_key = row_key
            super().__init__()

    BINDINGS = [
        Binding("ctrl+d", "remove_row", "Remove Path", show=True, priority=True),
        Binding("ctrl+p", "reveal_path", "Reveal Path", show=True, priority=True),
    ]

    column_headers = (
        ("icon", "", 2),
        ("current_name", "Current Name", None),
        ("new_name", "New Name", None),
    )
    current_sorts: set[str] = set()

    @on(Mount)
    def load_columns(self) -> None:
        self.cursor_type = "row"
        for key, label, width in self.column_headers:
            self.add_column(label, width=width, key=key)

    def load_paths_in_table(self, paths) -> dict[RowKey, PathRow]:
        """Load the provided system paths into the DataTable."""
        loaded_paths: dict[RowKey, PathRow] = {}
        for path in paths:
            path_row = PathRow(path, self)
            if not path_row.path.exists() or path_row in loaded_paths.values():
                continue
            self.add_row(*path_row.row_info, key=path_row.row_key.value)
            loaded_paths[path_row.row_key] = path_row
        return loaded_paths

    @on(DataTable.HeaderSelected)
    def sort_table_by_header(self, event: DataTable.HeaderSelected) -> None:
        """Sort table by clicked row header."""

        def sort_reverse(current_sorts: set[str], sort_type: str):
            """Determine if `sort_type` is ascending or descending."""
            try:
                current_sorts.remove(sort_type)
            except KeyError:
                current_sorts.add(sort_type)
            return sort_type in current_sorts

        column_key = event.column_key
        self.sort(column_key, reverse=sort_reverse(self.current_sorts, str(column_key)))

    def action_remove_row(self) -> None:
        """Delete the currently selected row (path)."""
        if not self.row_count:
            return
        row_key, _ = self.coordinate_to_cell_key(self.cursor_coordinate)
        self.remove_row(row_key)
        self.post_message(self.RemovePath(row_key))

    def action_reveal_path(self) -> None:
        """Reveal the currently selected row (path)."""
        if not self.row_count:
            return
        row_key, _ = self.coordinate_to_cell_key(self.cursor_coordinate)
        self.post_message(self.RevealPath(row_key))
