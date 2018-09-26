from hash_table import HashTable

import pytest

@pytest.fixture
def empty_table():
    return HashTable()

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
