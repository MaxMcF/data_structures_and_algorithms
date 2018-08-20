from .linked_list import LinkedList
import pytest

@pytest.fixture
def empty_list():
    return LinkedList()

@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exists():
    assert LinkedList


def test_create_instance_of_list():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    assert empty_list.head is None


def test_default_property_length(empty_list):
    assert empty_list._length == 0


def test_insert_successful(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    actual = small_list.includes(3)
    assert actual is True
    # assert small_list.includes(1) is True


def test_includes_returns_false_if_not_exists(small_list):
    assert small_list.includes(100) is False
    assert small_list.includes(0) is False


def test_repr_returns_correct_value(small_list):
    expected = '<Linked List | Head: 4 | Length: 4>'
    actual = repr(small_list)
    assert expected == actual


def test_str_returns_correct_value(small_list):
    expected = 'Head: 4 | Length: 4'
    actual = str(small_list)
    assert expected == actual


def test_append_return_true(small_list):
    expected = True
    actual = small_list.append(5)
    assert expected == actual


def test_insert_before_works(small_list):
    expected = True
    acutal = small_list.insert_before(10, 1)
    assert acutal == expected


def test_insert_after_works(small_list):
    expected = True
    acutal = small_list.insert_after(10, 4)
    assert acutal == expected


def test_insert_before_invalid_input(small_list):
    expected = False
    actual = small_list.insert_before(99999, None)
    assert actual == expected


def test_insert_after_invalid_input(small_list):
    expected = False
    actual = small_list.insert_before(99999, None)
    assert actual == expected







