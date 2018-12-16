import math


class Node():
    def __init__(self, name, neighbors):
        self.prev = None
        self.weight = math.inf
        self.name = name
        self.neighbors = neighbors

dij_map = {
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


def sort_weight(node):
    return node.weight


def dijkstra_alg(graph, start, end):
    """Step 1: Create the completed_nodes queue, and the priority_queue.
    Identify the first element in the queue based of the weight.
    (starting node should always have a weight of zero).
    """
    completed_nodes = []
    priority_queue = []
    path = []
    for node_name in graph.keys():
        if str(node_name) == start:
            first_node = Node(node_name, graph[node_name])
            first_node.weight = 0
            priority_queue.append(first_node)
        else:
            priority_queue.append(Node(node_name, graph[node_name]))
    priority_queue.sort(key=sort_weight)


    def _traverse(node):
        if len(priority_queue) < 1:
            print(priority_queue)
            return "Finished Traversal"
        for neighbor in node.neighbors:
            # ignore the node we are traversing from
            if neighbor != node.name:
                node_in_queue = None
                for priority_node in priority_queue:
                    if priority_node.name == neighbor:
                        node_in_queue = priority_node


                # priority_queue = dict(priority_queue))
                # node_in_queue = priority_queue.get(neighbor)
                if node_in_queue:
                    new_weight = node.weight + node.neighbors[neighbor]
                    if new_weight < node_in_queue.weight:
                        node_in_queue.weight = new_weight
                        node_in_queue.prev = node

        completed_nodes.append(node)
        priority_queue.sort(key=sort_weight)
        _traverse(priority_queue.pop(0))

    _traverse(priority_queue.pop(0))

    def _reverse_find(node):
        if node.prev is None:
            path.append(node)
            return "Path complete"
        path.append(node)
        _reverse_find(node.prev)


    for node in completed_nodes:
        if node.name == end:
            _reverse_find(node)


    return path

path = dijkstra_alg(dij_map, 'S', 'E')
path = path[::-1]
print([node.name for node in path])


