import pytest
from queue_with_stacks import Queue

@pytest.fixture
def small_queue():
    sq = Queue()
    sq.enqueue(5)
    sq.enqueue(4)
    sq.enqueue(3)
    sq.enqueue(2)
    return sq


def test_queue_exists():
    assert Queue

def test_enqueue_method(small_queue):
    actual = small_queue.dequeue()
    expected = 5
    assert actual == expected
