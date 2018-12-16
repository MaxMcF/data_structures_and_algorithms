import math


class Node():
    def __init__(self, name, neighbors):
        self.prev = None
        self.weight = math.inf
        self.name = name
        self.neighbors = neighbors


def sort_weight(node):
    return node.weight


def dijkstra_alg(graph, start, end):
    """Step 1: Create the completed_nodes queue, and the priority_queue.
    Identify the first element in the queue based of the weight.
    (starting node should always have a weight of zero).
    """

    if any(graph) is False:
        raise TypeError

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


    """Step 2: - Check all neighboring nodes of the starting node
    - Check the weights of the neighboring nodes. If they are less, reassign the values in the priority queue
    - Re-order the queue, with the lowest weight at the beginning.
    - Run this functionality recursively, until all nodes in the priority queue have been traversed.
    """


    def _traverse(node):

        if len(priority_queue) < 2:
            completed_nodes.append(priority_queue.pop(0))
            return "Finished Traversal"

        for neighbor in node.neighbors:

            if neighbor != node.name: # ignore the node we are traversing from

                node_in_queue = None
                for priority_node in priority_queue:
                    if priority_node.name == neighbor:
                        node_in_queue = priority_node

                if node_in_queue:
                    new_weight = node.weight + node.neighbors[neighbor]
                    if new_weight < node_in_queue.weight:
                        node_in_queue.weight = new_weight
                        node_in_queue.prev = node

        completed_nodes.append(priority_queue.pop(0))

        priority_queue.sort(key=sort_weight)
        _traverse(priority_queue[0])

    _traverse(priority_queue[0])


    """Step 3: Go through the completed node queue, tracing back the shortest path.
    """
    def _reverse_find(node):
        if node.prev is None:
            path.append(node)
            return "Path complete"
        path.append(node)
        _reverse_find(node.prev)


    for node in completed_nodes:
        if node.name == end:
            _reverse_find(node)

    path = [node.name for node in path]

    path = path[::-1]

    if path[0] == start and path[-1] == end:
        return path
    else:
        return "Invalid Graph"




