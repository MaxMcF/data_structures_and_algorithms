import pytest
from .a_star import a_star

@pytest.fixture()
def graph_empty():
    g = {}
    return g


@pytest.fixture()
def full_graph():
    g = {
    'A': {'Coords':(3, 8), 'Neighbors':{ 'S': 7, 'B': 3, 'D': 4,}},
    'B': {'Coords':(5, 7), 'Neighbors':{'S': 2, 'A': 3, 'D': 4, 'H': 1,}},
    'C': {'Coords':(10, 10), 'Neighbors':{'S': 3, 'L': 2,}},
    'D': {'Coords':(3, 5), 'Neighbors':{'A': 4, 'B': 4, 'F': 5,}},
    'H': {'Coords':(6, 4), 'Neighbors':{'B': 1, 'F': 3, 'G': 2,}},
    'F': {'Coords':(3, 2), 'Neighbors':{'D': 5, 'H': 3,}},
    'G': {'Coords':(7, 2), 'Neighbors':{'H': 2, 'E': 2,}},
    'S': {'Coords':(5, 10), 'Neighbors':{'A': 7, 'B': 2, 'C': 3,}},
    'L': {'Coords':(12, 7), 'Neighbors':{'C': 2, 'I': 4, 'J': 4}},
    'I': {'Coords':(11, 5), 'Neighbors':{'L': 4, 'J': 6, 'K': 4,}},
    'J': {'Coords':(13, 5), 'Neighbors':{'L': 4, 'I': 6, 'K': 4,}},
    'K': {'Coords':(12, 2), 'Neighbors':{'I': 4, 'J': 4, 'E': 5,}},
    'E': {'Coords':(9, 0), 'Neighbors':{'G': 2, 'K': 5}}
    }
    return g

@pytest.fixture()
def smaller_graph():
    g = {'A':{'Coords':(2,4), 'Neighbors':{'C': 2, 'B': 1,}},
        'B':{'Coords':(2,4), 'Neighbors':{'A': 1, 'D': 4,}},
        'C':{'Coords':(2,4), 'Neighbors':{'A': 2, 'D': 2,}},
        'D':{'Coords':(2,4), 'Neighbors':{'B': 4, 'C': 2,}},
    }
    return g



@pytest.fixture()
def smaller_graph_diff_coords():
    g = {'A':{'Coords':(2,4), 'Neighbors':{'C': 2, 'B': 1,}},
        'B':{'Coords':(2,17), 'Neighbors':{'A': 1, 'D': 4,}},
        'C':{'Coords':(2,8), 'Neighbors':{'A': 2, 'D': 2,}},
        'D':{'Coords':(2,18), 'Neighbors':{'B': 4, 'C': 2,}},
    }
    return g




def test_simple_traversal(smaller_graph):
    actual = a_star(smaller_graph, 'A', 'D')
    expected = ['A', 'C', 'D']
    assert actual == expected

def test_simple_traversal_with_heuristics(smaller_graph_diff_coords):
    actual = a_star(smaller_graph_diff_coords, 'A', 'D')
    expected = ['A', 'B', 'D']
    assert actual == expected

def test_complex_traversal(full_graph):
    actual = a_star(full_graph, 'S', 'E')
    expected = ['S', 'B', 'H', 'G', 'E']
    assert actual == expected

def test_complex_traversal_diff_start_and_end(full_graph):
    actual = a_star(full_graph, 'K', 'D')
    expected = ['K', 'E', 'G', 'H', 'B', 'D']
    assert actual == expected


def test_empty_graph_returns_error(graph_empty):
    with pytest.raises(TypeError):
        a_star(graph_empty, 'A', 'F')

