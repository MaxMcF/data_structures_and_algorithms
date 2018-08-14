from .array_shift import insert_shift_array
import pytest

def test_insert_shift_array_exists():
    assert insert_shift_array


def test_insert_shift_array_returns_simple_list():
    expected = [1,2,3,4,5]
    actual = insert_shift_array([1,2,4,5], 3)
    assert actual == expected


def test_returns_error_on_null():
    with pytest.raises(TypeError):
        insert_shift_array(None)


def test_insert_shift_array_returns_complex_list():
    expected = [-1,-5,-8,0,6,9]
    actual = insert_shift_array([-1,-5,-8,6,9], 0)
    assert actual == expected



