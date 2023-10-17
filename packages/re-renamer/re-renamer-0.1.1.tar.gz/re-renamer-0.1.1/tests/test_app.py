import random

import pytest
from textual.widgets import Checkbox, Footer, Header, RichLog

from re_renamer.app import REnamer
from re_renamer.widgets import Buttons, Inputs, Log, Options, Table


def test_app_creation(app):
    assert app.title == "[RE]namer"


def test_app_paths(app, paths):
    path = random.choice(paths)
    assert path in app._paths


@pytest.mark.asyncio
async def test_app_compose(app):
    async with app.run_test():
        assert app.query_one(Header)
        assert app.query_one(Footer)
        assert app.query_one(Table)
        assert app.query_one(Options)
        assert app.query_one(Inputs)
        assert app.query_one(Buttons)
        assert app.query_one(Log)


@pytest.mark.asyncio
async def test_load_paths(tmp_path):
    f = tmp_path.joinpath("f.txt")
    f.touch()
    app = REnamer([f])
    async with app.run_test():
        assert f in [path_row.path for path_row in app.paths.values()]


@pytest.mark.asyncio
async def test_activity_log_clear(app):
    async with app.run_test() as pilot:
        log = app.query_one(Log)
        rich_log = log.query_one("#rich-log", RichLog)
        assert not rich_log.lines
        rich_log.focus()
        await pilot.press("ctrl+d")
        assert not rich_log.lines


@pytest.mark.asyncio
async def test_reset_button(paths):
    app = REnamer(
        paths, case_sensitive=True, first_match=True, overwrite_protection=False
    )
    async with app.run_test() as pilot:
        table = app.query_one(Table)
        assert table.row_count == len(app.paths)
        case_sensitive = app.query_one("#case-sensitive", Checkbox)
        first_match = app.query_one("#first-match", Checkbox)
        await pilot.click("#reset")
        assert not case_sensitive.value
        assert not app.case_sensitive
        assert not first_match.value
        assert not app.first_match
        assert app.overwrite_protection
