from .fifo_animal_shelter import AnimalShelter
import pytest

@pytest.fixture
def empty_shelter():
    shelter = AnimalShelter()
    return shelter

@pytest.fixture
def small_shelter():
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('cat')
    return shelter


def test_animal_shelter_init(empty_shelter):
    actual = empty_shelter.enqueue('dog')
    expected = 'dog'
    assert str(actual) == expected

def test_animal_shelter_populate(small_shelter):
    actual = len(small_shelter)
    expected = 6
    assert actual == expected

def test_animal_shelter_dequeue(small_shelter):
    actual = small_shelter.dequeue('cat')
    expected = 'cat'
    assert actual == expected
