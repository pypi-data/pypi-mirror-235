import pytest

from re_renamer import REGEX_LOG_FP
from re_renamer.widgets import Table


@pytest.mark.asyncio
async def test_rename_no_table_rows(app):
    async with app.run_test():
        table = app.query_one(Table)
        assert table.row_count == len(app.paths)
        for row_key, _ in app.paths.items():
            table.remove_row(row_key)
        assert table.row_count == 0
        assert app.query_one("#rename").disabled


@pytest.mark.asyncio
async def test_rename_no_find_value(app):
    async with app.run_test():
        table = app.query_one(Table)
        assert table.row_count == len(app.paths)
        assert app.query_one("#rename").disabled


@pytest.mark.asyncio
async def test_rename_function(app, paths):
    for p in paths:
        p.touch()
    async with app.run_test() as pilot:
        find = app.query_one("#find")
        find.value = "test_path"
        replace = app.query_one("#replace")
        replace.value = "check"
        await pilot.click("#rename")
        for path_row in app.paths.values():
            assert "check" in path_row.path.name
            assert path_row.path.match("*check*")
            assert "test_path" not in path_row.path.name
            assert not path_row.path.match("*test_path*")


@pytest.mark.asyncio
async def test_rename_history_write(app):
    async with app.run_test() as pilot:
        find = app.query_one("#find")
        find.value = "test_path"
        replace = app.query_one("#replace")
        replace.value = "check"
        await pilot.click("#rename")
        with open(REGEX_LOG_FP) as f:
            last_line = f.readlines()[-1]
            assert find.value in last_line
            assert replace.value in last_line
