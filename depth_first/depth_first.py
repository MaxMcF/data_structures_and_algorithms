class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return f'< Graph_Size: {len(self.graph)}>'

    def __str__(self):
        return f'Graph Size: {len(self.graph)}'

    def __len__(self):
        return len(self.graph)

    def add_node(self, val):
        """
        """
        if self._has_vert(val) is False:
            self.graph[val] = {}
        else:
            raise Exception
        # Use val to create new Vertice
        # add vertice to self.graph
        # check to see if the ver already exists: if so, raise expection
            # create helper method

    def _has_vert(self, val):
        """
        """
        for key in self.graph.keys():
            if key == val:
                return True
        return False

        # check for a key in the graph

    def add_edge(self, vert_one, vert_two, weight):
        """
        """
        if vert_two not in self.graph[vert_one]:
            self.graph[vert_one].update({vert_two: weight})
        else:
            raise Exception
        # add a relationship and weight between two verts
        # don't forget to validate

    def get_neighbors(self, val):
        """
        """
        if val in self.graph:
            return self.graph[val]
        else:
            raise Exception
        # Given a val (key), return all adjecent verts

    def breadth_first(self, start_vert):
        """This traverses the graph and returns the entiriety of it
        """
        vert_list = []
        def _walk(vert):
            vert_relations = self.get_neighbors(vert)
            for relation in vert_relations:
                if relation not in vert_list:
                    vert_list.append(relation)
                    _walk(relation)
        vert_list.append(start_vert)
        _walk(start_vert)
        return vert_list

    def depth_first(self, start_vert):
        """This will traverse a graph
        """
        vert_list = []
        def _walk(vert):
            vert_relations = self.get_neighbors(vert)
            vert_list.append(vert)
            for relation in vert_relations:
                if relation not in vert_list:
                    _walk(relation)
        _walk(start_vert)
        return vert_list
