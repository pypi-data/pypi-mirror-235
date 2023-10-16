import pytest


@pytest.mark.asyncio
async def test_find_input_invalid(app):
    async with app.run_test() as pilot:
        find = app.query_one("#find")
        find.focus()
        find_error = app.query_one("#find-error")
        assert not find_error.render()
        await pilot.press("[")
        assert find_error.render()


@pytest.mark.asyncio
async def test_replace_input_invalid(app):
    async with app.run_test() as pilot:
        replace_error = app.query_one("#replace-error")
        assert not replace_error.render()
        replace = app.query_one("#replace")
        replace.focus()
        await pilot.press("\\")
        assert replace_error.render()
