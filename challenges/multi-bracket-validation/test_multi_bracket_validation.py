import pytest
from multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_val_exists():
    assert multi_bracket_validation

def test_multi_bracket_val_returns_true_simple():
    actual = multi_bracket_validation('()')
    expected = True
    assert actual == expected

def test_multi_bracket_val_returns_false_simple():
    actual = multi_bracket_validation('((')
    expected = False
    assert actual == expected

def test_multi_bracket_val_returns_false_simple_end_brackets():
    actual = multi_bracket_validation('}}')
    expected = False
    assert actual == expected

def test_multi_bracket_val_returns_false_complex():
    actual = multi_bracket_validation('(){{()}}(((())))[[{[}]]')
    expected = False
    assert actual == expected

def test_multi_bracket_val_returns_true_complex():
    actual = multi_bracket_validation('((()))[{({})}]{()}{}')
    expected = True
    assert actual == expected

def test_multi_bracket_val_returns_true_with_string():
    actual = multi_bracket_validation('((this is a string))')
    expected = True
    assert actual == expected

def test_multi_bracket_val_returns_type_error():
    with pytest.raises(TypeError):
        multi_bracket_validation(1232321)

def test_multi_bracket_val_returns_type_error_on_null():
    with pytest.raises(TypeError):
        multi_bracket_validation(None)

