import pytest
from .bst import BinaryTree, find_maximum

@pytest.fixture
def large_binary_tree():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    return bt

@pytest.fixture
def small_binary_tree():
    bt = BinaryTree([10, 4, 39])
    return bt

def test_class_exists():
    assert BinaryTree

def test_binary_tree_initializes():
    assert BinaryTree([1,2,3])

def test_binary_tree_insert(large_binary_tree):
    large_binary_tree.insert(5)
    actual = large_binary_tree.in_order()
    expected = [5,11,12,14,18,19,20,22,31,33,40]
    assert actual == expected

def test_in_order(small_binary_tree):
    actual = small_binary_tree.in_order()
    expected = [4, 10, 39]
    assert actual == expected

def test_pre_order(small_binary_tree):
    actual = small_binary_tree.pre_order()
    expected = [10, 4, 39]
    assert actual == expected

def test_post_order(small_binary_tree):
    actual = small_binary_tree.post_order()
    expected = [4, 39, 10]
    assert actual == expected

def test_duplicate_val_case(small_binary_tree):
    actual = small_binary_tree.insert(4)
    expected = 'Error, cannot accept duplicates!'
    assert actual == expected

def test_none_value_error(small_binary_tree):
    with pytest.raises(TypeError):
        small_binary_tree.insert(None)

def test_negative_vals(small_binary_tree):
    small_binary_tree.insert(-50)
    actual = small_binary_tree.in_order()
    expected = [-50,4,10,39]
    assert actual == expected

def test_type_error_on_string_input(small_binary_tree):
    with pytest.raises(TypeError):
        small_binary_tree.insert('Failure')

def test_max_function_exists():
    assert find_maximum

def test_max_function_works_small_tree(small_binary_tree):
    actual = find_maximum(small_binary_tree)
    expected = 39
    assert actual == expected

def test_max_function_works_large_tree(large_binary_tree):
    actual = find_maximum(large_binary_tree)
    expected = 40
    assert actual == expected

def test_max_function_gives_error_null_input():
    with pytest.raises(AttributeError):
        find_maximum(None)

def test_max_function_gives_one_val_on_duplicates():
    actual = find_maximum(BinaryTree([55,55,55,55,55,55,55,55,55]))
    expected = 55
    assert actual == expected

