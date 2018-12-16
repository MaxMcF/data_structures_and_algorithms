import math


class Node():
    def __init__(self, name, neighbors, coord, end_node=None):
        self.prev = None
        self.weight = math.inf
        self.name = name
        self.neighbors = neighbors
        self.coord = coord
        self.end_node = end_node

    def calc_heuristic(self):
        if self.end_node is None:
            return 0
        x_dist = abs(self.coord[0] - self.end_node.coord[0])
        y_dist = abs(self.coord[1] - self.end_node.coord[1])
        if x_dist is 0:
            return y_dist
        if y_dist is 0:
            return x_dist
        return math.sqrt((x_dist**2) + (y_dist**2))




def sort_weight(node):
    return node.weight + node.calc_heuristic()


def a_star(graph, start, end):
    """Step 1: Create the completed_nodes queue, and the priority_queue.
    Identify the first element in the queue and assign a weight of zero.
    (starting node should always have a weight of zero).
    Initialize the end_node instance of the Node class, which allows all other nodes to refrence it.
    """

    if any(graph) is False:
        raise TypeError

    completed_nodes = []
    priority_queue = []
    path = []

    end_node_instance = Node(end, graph[end]['Neighbors'], graph[end]['Coords'])
    priority_queue.append(end_node_instance)

    for node_name in graph.keys():
        if node_name != end:
            if str(node_name) == start:
                first_node = Node(node_name, graph[node_name]['Neighbors'], graph[node_name]['Coords'], end_node_instance)
                first_node.weight = 0
                priority_queue.append(first_node)
            else:
                priority_queue.append(Node(node_name, graph[node_name]['Neighbors'], graph[node_name]['Coords'], end_node_instance))

    priority_queue.sort(key=sort_weight)


    """Step 2: - Check all neighboring nodes of the starting node
    - Check the heuristic weights of the neighboring nodes. If they are less, reassign the values in the priority queue
    - Re-order the queue, with the lowest weight at the beginning.
    - Run this functionality recursively, until the end node has been reached.
    """


    def _traverse(node):

        if node.name == end:
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





