from re_renamer.widgets.inputs import ValidFindRegex, ValidSubstitutionRegex


def test_valid_regex():
    validator = ValidFindRegex()
    result = validator.validate("A")
    assert result.is_valid


def test_invalid_regex():
    validator = ValidFindRegex()
    result = validator.validate("[")
    assert not result.is_valid


def test_valid_substitution():
    validator = ValidSubstitutionRegex()
    result = validator.validate("\\1", "(.)")
    assert result.is_valid


def test_invalid_substitution():
    validator = ValidSubstitutionRegex()
    result = validator.validate("\\1", ".")
    assert not result.is_valid
