from queue import Queue
import pytest

@pytest.fixture
def small_queue():
    sq = Queue([1,2,3,4,5])
    return sq

def test_queue_init(small_queue):
    actual = len(small_queue)
    expected = 5
    assert actual == expected

def test_enqueue_works(small_queue):
    actual = small_queue.enqueue(6)
    expected = 6
    assert actual == expected

def test_dequeue_works(small_queue):
    actual = small_queue.dequeue()
    expected = 1
    assert actual == expected

def test_queue_str_magic_method(small_queue):
    actual = str(small_queue)
    expected = 'Queue Front: 1 | Queue Back: 5 | Stack Length: 5'
    assert actual == expected
