import pytest

from re_renamer.text_plus import TextPlus


def test_lt():
    s1 = TextPlus("abc")
    s2 = TextPlus("xyz")
    assert s1 < s2
    assert not s1 > s2


def test_lt_error():
    s1 = TextPlus("abc")
    s2 = ["xyz"]
    with pytest.raises(TypeError):
        s1 < s2


def test_le():
    s1 = TextPlus("abc")
    s2 = TextPlus("xyz")
    assert s1 <= s2
    assert not s1 >= s2


def test_le_error():
    s1 = TextPlus("abc")
    s2 = ["xyz"]
    with pytest.raises(TypeError):
        s1 <= s2


def test_gt():
    s1 = TextPlus("abc")
    s2 = TextPlus("xyz")
    assert s2 > s1
    assert not s2 < s1


def test_gt_error():
    s1 = TextPlus("abc")
    s2 = ["xyz"]
    with pytest.raises(TypeError):
        s2 > s1


def test_ge():
    s1 = TextPlus("abc")
    s2 = TextPlus("xyz")
    assert s2 >= s1
    assert not s2 <= s1


def test_ge_error():
    s1 = TextPlus("abc")
    s2 = ["xyz"]
    with pytest.raises(TypeError):
        s2 >= s1
