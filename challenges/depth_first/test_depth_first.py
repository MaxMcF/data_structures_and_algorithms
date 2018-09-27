import pytest
from .depth_first import Graph


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

def test_breadth_first_works(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.breadth_first('A')
    expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert actual == expected

def test_breadth_first_small_graph(graph_filled):
    actual = graph_filled.breadth_first('A')
    expected = ['A', 'B', 'D', 'C']
    assert actual == expected

def test_breadth_first_handles_error(graph_filled):
    with pytest.raises(Exception):
        graph_filled.breadth_first(123409182735091827359)

def test_breadth_first_handles_single_node_graph():
    g = Graph()
    g.add_node('E')
    actual = g.breadth_first('E')
    expected = ['E']
    assert actual == expected

def test_depth_first(graph_filled_for_traversal):
    actual = graph_filled_for_traversal.depth_first('A')
    expected = ['A', 'B', 'D', 'E', 'C', 'F', 'G']
    assert actual == expected

def test_depth_first_small_graph(graph_filled):
    import pdb; pdb.set_trace()
    actual = graph_filled.depth_first('A')
    expected = ['A', 'B', 'D', 'C']
    assert actual == expected

def test_depth_first_error_handling(graph_empty):
    with pytest.raises(Exception):
        graph_empty.depth_first(12345123)

def test_depth_first_handles_single_vert_graph(graph_empty):
    graph_empty.add_node('E')

    actual = graph_empty.depth_first('E')
    expected = ['E']
    assert actual == expected
