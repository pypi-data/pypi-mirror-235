import pytest

from re_renamer import ICONS
from re_renamer.widgets import Table


@pytest.mark.asyncio
async def test_datatable_remove_row(app, paths):
    async with app.run_test() as pilot:
        table = app.query_one(Table)
        assert table.row_count == len(app.paths)
        await pilot.click(Table)
        await pilot.press("ctrl+d")
        assert table.row_count == len(paths) - 1


@pytest.mark.asyncio
async def test_path_reset_after_input_change(app):
    async with app.run_test() as pilot:
        table = app.query_one(Table)
        row_key = list(app.paths.keys())[0]
        _, current_name, new_name = table.get_row(row_key)
        assert current_name == new_name.plain
        await pilot.click("#first-match")
        assert app.query_one("#first-match").value
        await pilot.click("#find")
        await pilot.press(".")
        assert app.query_one("#find").value == "."
        _, current_name, new_name = table.get_row(row_key)
        assert current_name != new_name.plain
        await pilot.press("backspace")
        _, current_name, new_name = table.get_row(row_key)
        assert current_name == new_name.plain


@pytest.mark.asyncio
async def test_path_new_path_exists_alert(app):
    async with app.run_test() as pilot:
        table = app.query_one(Table)
        row_key = list(app.paths.keys())[0]
        find = app.query_one("#find")
        find.focus()
        await pilot.press("0")
        replace = app.query_one("#replace")
        replace.focus()
        await pilot.press("1")
        icon, _, _ = table.get_row(row_key)
        assert icon == ICONS["alert"]
