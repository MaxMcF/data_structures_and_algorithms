import pytest
from stack import Stack

@pytest.fixture
def small_stack():
    ss = Stack([1,2,3,4,5])
    return ss

def test_stack_init(small_stack):
    actual = len(small_stack)
    expected = 5
    assert actual == expected

def test_stack_push(small_stack):
    actual = small_stack.push(6)
    expected = 6
    assert actual == expected

def test_stack_pop(small_stack):
    actual = small_stack.pop()
    expected = 5
    assert actual == expected

def test_stack_peek(small_stack):
    actual = small_stack.peek()
    expected = '< Value: 5 | Next: 4 >'
    assert str(actual) == expected

