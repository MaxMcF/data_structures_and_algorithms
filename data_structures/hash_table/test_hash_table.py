from .hash_table import HashTable

import pytest

@pytest.fixture
def empty_table():
    ht = HashTable()
    return ht

@pytest.fixture
def filled_table():
    ht = HashTable()
    ht.set('Max', 'Max Gunnar McFarland')
    return ht

@pytest.fixture
def big_table():
    ht = HashTable()
    ht.set('Max', 'Max Gunnar McFarland')
    ht.set('Mike', 'Michael Jordan')
    ht.set('John', 'John Hamm')
    ht.set('Charlie', 'Tiger Blood')
    ht.set('Ben', 'Ben Heimershmidt')
    ht.set('Charlize', 'Charlieze Theron')
    ht.set('Brian', 'Brian Cranston')
    ht.set('J', 'J Christie')
    ht.set('Alex', 'Alexander Stone')
    ht.set('Barrack', 'Barrack Hussien Obama')
    ht.set('Garp', 'Garp Taco Sanchez')
    ht.set('Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.')
    return ht

def test_hash_table_exists():
    assert HashTable

def test_hash_table_get(filled_table):
    actual = filled_table.get('Max')
    expected = 'Max Gunnar McFarland'
    assert actual == expected

def test_hash_table_remove(filled_table):
    filled_table.remove('Max')
    with pytest.raises(TypeError):
        filled_table.get('Max')

def test_hash_table_larger_table_get(big_table):
    actual = big_table.get('Alf')
    expected = 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.'
    assert actual == expected

def test_hash_table_larger_delete(big_table):
    big_table.remove('Brian')
    with pytest.raises(TypeError):
        big_table.get('Brian')

def test_hash_table_raises_error_null_key(empty_table):
    with pytest.raises(TypeError):
        empty_table.set(None, 'This is a Test')

def test_hash_table_raises_no_error_null_value(empty_table):
    empty_table.set('test', None)
    actual = empty_table.get('test')
    expected = None
    assert actual == expected

def test_hash_table_raises_error_on_null_value_remove(filled_table):
    with pytest.raises(TypeError):
        filled_table.remove('test')

def test_hash_table_raise_error_on_collision(filled_table):
    with pytest.raises(TypeError):
        filled_table.set('Max', 'The Destroyer!!')
