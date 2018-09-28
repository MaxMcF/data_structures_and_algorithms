from merge_sort import merge_sort
import random
import pytest


@pytest.fixture
def large_list():
    return [32,123,43,3,2,5,7,8,9,0,4355,65,1231,98,900,2123,432,4554554]

@pytest.fixture
def really_big_list():
    big_list = []
    counter = 10000
    while counter:
        ran_num = random.randint(0, 10000)
        big_list.append(ran_num)
        counter -= 1
    return big_list

def test_selection_sort():
    assert merge_sort

def test_large_list(large_list):
    actual = merge_sort(large_list)
    assert all(actual[i] <= actual[i+1] for i in range(len(actual)-1))

def test_really_big_list(really_big_list):
    actual = merge_sort(really_big_list)
    assert all(actual[i] <= actual[i+1] for i in range(len(actual)-1))

def test_repeated_num_list():
    actual = merge_sort([7,7,7,7,7,7,7,7,7,7,4,7])
    assert all(actual[i] <= actual[i+1] for i in range(len(actual)-1))


