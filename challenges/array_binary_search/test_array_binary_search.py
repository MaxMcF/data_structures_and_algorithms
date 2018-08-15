from .array_binary_search import binary_search
import pytest

def test_binary_search_exists():
    assert binary_search


def test_binary_search_odd_array():
    expected = 2
    actual = binary_search([1,2,3,4,5], 3)
    assert actual == expected


def test_binary_search_even_array():
    expected = 9
    actual = binary_search([20,40,60,80,100, 120, 140, 160, 180, 200, 220, 221, 222, 223], 200)
    assert actual == expected


def test_binary_search_empty_array():
    expected = -1
    actual = binary_search([], 3)
    assert actual == expected


def test_binary_search_type_error():
    with pytest.raises(TypeError):
        binary_search([1,2,3,4,5], 'some string')
