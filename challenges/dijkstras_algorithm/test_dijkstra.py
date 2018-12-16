import pytest
from .dijkstra import dijkstra_alg

@pytest.fixture()
def graph_empty():
    g = {}
    return g


@pytest.fixture()
def full_graph():
    g = {
    'A': {'S': 7, 'B': 3, 'D': 4,},
    'B': {'S': 2, 'A': 3, 'D': 4, 'H': 1,},
    'C': {'S': 3, 'L': 2,},
    'D': {'A': 4, 'B': 4, 'F': 5,},
    'H': {'B': 1, 'F': 3, 'E': 4,},
    'F': {'D': 5, 'H': 3,},
    'S': {'A': 7, 'B': 2, 'C': 3,},
    'L': {'C': 2, 'I': 4, 'J': 4},
    'I': {'L': 4, 'J': 6, 'K': 4,},
    'J': {'L': 4, 'I': 6, 'K': 4,},
    'K': {'I': 4, 'J': 4, 'E': 5,},
    'E': {'H': 4, 'K': 5}
    }
    return g

@pytest.fixture()
def smaller_graph():
    g = {'A': {'C': 2, 'B': 1,},
    'B': {'A': 1, 'D': 4,},
    'C': {'A': 2, 'D': 2,},
    'D': {'B': 4, 'C': 2,},
    }
    return g


@pytest.fixture()
def no_solution_graph():
    g = {'A': {'C': 2, 'B': 1,},
    'B': {'A': 1, 'D': 4,},
    'C': {'A': 2, 'D': 2,},
    'D': {'B': 4, 'C': 2,},
    'E': {'F': 4},
    'F': {'E': 4},
    }
    return g



@pytest.fixture()
def loop_graph():
    g = {'A': {'B': 2, 'F': 1,},
    'B': {'A': 2, 'C': 4,},
    'C': {'B': 4, 'D': 2,},
    'D': {'E': 4, 'C': 2,},
    'E': {'D': 4, 'F': 1,},
    'F': {'E': 1, 'A': 1,},
    }
    return g




def test_simple_traversal(smaller_graph):
    actual = dijkstra_alg(smaller_graph, 'A', 'D')
    expected = ['A', 'C', 'D']
    assert actual == expected

def test_complex_traversal(full_graph):
    actual = dijkstra_alg(full_graph, 'S', 'E')
    expected = ['S', 'B', 'H', 'E']
    assert actual == expected

def test_no_solution_graph(no_solution_graph):
    actual = dijkstra_alg(no_solution_graph, 'A', 'E')
    expected = "Invalid Graph"
    assert actual == expected

def test_single_edge_shortest(loop_graph):
    actual = dijkstra_alg(loop_graph, 'A', 'F')
    expected = ['A', 'F']
    assert actual == expected

def test_empty_graph_returns_error(graph_empty):
    with pytest.raises(TypeError):
        dijkstra_alg(graph_empty, 'A', 'F')

