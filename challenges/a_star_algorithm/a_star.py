import math




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
    Identify the first element in the queue based of the weight.
    (starting node should always have a weight of zero).
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
    - Check the weights of the neighboring nodes. If they are less, reassign the values in the priority queue
    - Re-order the queue, with the lowest weight at the beginning.
    - Run this functionality recursively, until all nodes in the priority queue have been traversed.
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


path = a_star(g, 'B', 'K')
print(path)



