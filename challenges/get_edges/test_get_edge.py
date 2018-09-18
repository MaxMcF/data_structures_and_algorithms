import pytest
from get_edge import Graph


@pytest.fixture()
def graph_empty():
    g = Graph()
    return g


@pytest.fixture()
def graph_filled():
    g = Graph()
    g.graph = {
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {},
        'D': {'A': 5},
        'E': {},
        'F': {}
    }
    return g


@pytest.fixture()
def graph_filled_for_traversal():
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g


def test_graph_exists():
    assert Graph

def test_graph_insert_single_val(graph_empty):
    graph_empty.add_node('A')
    assert graph_empty.graph['A'] == {}

def test_graph_add_neighbor_weight(graph_empty):
    graph_empty.add_node('A')
    graph_empty.add_edge('A', 'B', 10)
    assert graph_empty.graph['A'] == {'B': 10}

def test_graph_get_neighbors(graph_filled):
    actual = graph_filled.get_neighbors('B')
    expected = {'A': 5, 'D': 15, 'C': 20}
    assert actual == expected

def test_graph_raises_execption_on_duplicate_node(graph_empty):
    graph_empty.add_node('A')
    with pytest.raises(Exception):
        graph_empty.add_node('A')

def test_graph_raises_exception_on_get_neighbors_no_node(graph_filled):
    with pytest.raises(Exception):
        graph_filled.get_neighbors('H')

def test_graph_add_multiple_nodes_breaks(graph_empty):
    with pytest.raises(Exception):
        graph_empty.add_node('A', 'B')

def test_graph_add_node_works_with_integers(graph_empty):
    graph_empty.add_node(1)
    assert graph_empty.graph[1] == {}

def test_graph_add_edge_with_no_weight_breaks(graph_filled):
    with pytest.raises(Exception):
        graph_filled.add_edge('A', 'D')

def test_graph_add_edge_to_existing_node_with_no_existing_edges(graph_filled):
    graph_filled.add_edge('C', 'A', 30)
    assert graph_filled.graph['C'] == {'A': 30}

def test_get_neighbor_gets_empty_dict_on_no_val(graph_filled):
    actual = graph_filled.get_neighbors('C')
    expected = {}
    assert actual == expected

def test_get_edges_small_graph(graph_filled):
    actual = graph_filled.get_edges(['A', 'B'])
    expected = (True, 10)
    assert actual == expected

def test_get_edges_small_graph_more_destinations(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.get_edges(['A', 'B', 'C', 'G', 'F'])
    expected = (True, 57)
    assert actual == expected

def test_get_edges_returns_false_on_bad_path(graph_filled):
    actual = graph_filled.get_edges(['A', 'C'])
    expected = (False, 0)
    assert actual == expected

def test_get_edges_returns_false_bad_path_long(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.get_edges(['A', 'B', 'C', 'G', 'F', 'C'])
    expected = (False, 0)
    assert actual == expected

def test_get_edges_raises_type_error_on_bad_input(graph_filled_for_traversal):
    with pytest.raises(TypeError):
        graph_filled_for_traversal.get_edges(12345)

def test_get_edges_self_refrences(graph_filled):
    actual = graph_filled.get_edges(['A', 'B', 'D', 'A', 'B', 'D'])
    expected = (True, 55)
    assert actual == expected
