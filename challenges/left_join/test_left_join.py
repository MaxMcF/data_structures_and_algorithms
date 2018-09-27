from left_join import left_join
from hash_table import HashTable
import pytest


@pytest.fixture
def hash_table_filled_one_small():
    ht = HashTable()
    ht.set('Max', 'Max Gunnar McFarland')
    ht.set('Mike', 'Michael Jordan')
    ht.set('John', 'John Hamm')
    return ht

@pytest.fixture
def hash_table_filled_two_small():
    ht = HashTable()
    ht.set('Sonya', 'Sonya Sotomayor')
    ht.set('Mike', 'Michael Jackson')
    ht.set('John', 'John Wayne')
    return ht

@pytest.fixture
def hash_table_filled_one():
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

@pytest.fixture
def hash_table_filled_two():
    ht = HashTable()
    ht.set('Max', 'The Axe')
    ht.set('Mike', 'Michael Jackson')
    ht.set('John', 'John Wayne')
    ht.set('Charlie', 'Charlie Sheen')
    ht.set('Ben', 'Ben Allen')
    ht.set('Charlize', 'Mr. F')
    ht.set('Brian', 'Bad Luck')
    ht.set('J', 'Homer Simpson')
    ht.set('Gary', 'Gary Johnson')
    ht.set('Ruth', 'Ruth Bayner Ginsberg')
    ht.set('Sonya', 'Sonya Sotomayor')
    return ht

def test_left_join():
    assert left_join

def test_left_join_small_lists(hash_table_filled_one_small, hash_table_filled_two_small):
    actual = left_join(hash_table_filled_one_small, hash_table_filled_two_small)
    expected = [
        ['Max', 'Max Gunnar McFarland', None],
        ['John', 'John Hamm', 'John Wayne'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
    ]
    assert actual == expected

def test_left_join_big_lists_one(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[0] in actual

def test_left_join_big_lists_two(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[1] in actual

def test_left_join_big_lists_three(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[2] in actual

def test_left_join_big_lists_four(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[3] in actual

def test_left_join_big_lists_five(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[4] in actual

def test_left_join_big_lists_six(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[5] in actual

def test_left_join_big_lists_seven(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[6] in actual

def test_left_join_big_lists_eight(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[7] in actual

def test_left_join_big_lists_nine(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[8] in actual

def test_left_join_big_lists_ten(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[9] in actual

def test_left_join_big_lists_eleven(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[10] in actual

def test_left_join_big_lists_twelve(hash_table_filled_one, hash_table_filled_two):
    actual = left_join(hash_table_filled_one, hash_table_filled_two)
    expected = [
        ['Max', 'Max Gunnar McFarland', 'The Axe'],
        ['Mike', 'Michael Jordan', 'Michael Jackson'],
        ['John', 'John Hamm', 'John Wayne'],
        ['Charlie', 'Tiger Blood', 'Charlie Sheen'],
        ['Ben', 'Ben Heimershmidt', 'Ben Allen'],
        ['Charlize', 'Charlieze Theron', 'Mr. F'],
        ['Brian', 'Brian Cranston', 'Bad Luck'],
        ['J', 'J Christie', 'Homer Simpson'],
        ['Alex', 'Alexander Stone', None],
        ['Barrack', 'Barrack Hussien Obama', None],
        ['Garp', 'Garp Taco Sanchez', None],
        ['Alf', 'Alf, from that TV show. You know the one.... what was it called?...... Oh yeah Alf.', None],
    ]
    assert expected[11] in actual

def test_left_join_big_lists_reversed_one(hash_table_filled_two, hash_table_filled_one):
    actual = left_join(hash_table_filled_two, hash_table_filled_one)
    expected = [
        ['Max', 'The Axe', 'Max Gunnar McFarland'],
        ['Mike', 'Michael Jackson', 'Michael Jordan'],
        ['John', 'John Wayne', 'John Hamm'],
        ['Charlie', 'Charlie Sheen', 'Tiger Blood'],
        ['Ben', 'Ben Allen', 'Ben Heimershmidt'],
        ['Charlize', 'Mr. F', 'Charlieze Theron'],
        ['Brian', 'Bad Luck', 'Brian Cranston'],
        ['J', 'Homer Simpson', 'J Christie'],
        ['Gary', 'Gary Johnson', None],
        ['Ruth', 'Ruth Bayner Ginsberg', None],
        ['Sonya', 'Sonya Sotomayor', None],
    ]
    assert expected[10] in actual

def test_left_join_big_lists_reversed_two(hash_table_filled_two, hash_table_filled_one):
    actual = left_join(hash_table_filled_two, hash_table_filled_one)
    expected = [
        ['Max', 'The Axe', 'Max Gunnar McFarland'],
        ['Mike', 'Michael Jackson', 'Michael Jordan'],
        ['John', 'John Wayne', 'John Hamm'],
        ['Charlie', 'Charlie Sheen', 'Tiger Blood'],
        ['Ben', 'Ben Allen', 'Ben Heimershmidt'],
        ['Charlize', 'Mr. F', 'Charlieze Theron'],
        ['Brian', 'Bad Luck', 'Brian Cranston'],
        ['J', 'Homer Simpson', 'J Christie'],
        ['Gary', 'Gary Johnson', None],
        ['Ruth', 'Ruth Bayner Ginsberg', None],
        ['Sonya', 'Sonya Sotomayor', None],
    ]
    assert expected[7] in actual

def test_left_join_big_lists_reversed_three(hash_table_filled_two, hash_table_filled_one):
    actual = left_join(hash_table_filled_two, hash_table_filled_one)
    expected = [
        ['Max', 'The Axe', 'Max Gunnar McFarland'],
        ['Mike', 'Michael Jackson', 'Michael Jordan'],
        ['John', 'John Wayne', 'John Hamm'],
        ['Charlie', 'Charlie Sheen', 'Tiger Blood'],
        ['Ben', 'Ben Allen', 'Ben Heimershmidt'],
        ['Charlize', 'Mr. F', 'Charlieze Theron'],
        ['Brian', 'Bad Luck', 'Brian Cranston'],
        ['J', 'Homer Simpson', 'J Christie'],
        ['Gary', 'Gary Johnson', None],
        ['Ruth', 'Ruth Bayner Ginsberg', None],
        ['Sonya', 'Sonya Sotomayor', None],
    ]
    assert expected[4] in actual
