class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Value: {self.value} | Data: {self.data}'
    def __repr__(self):
        return f'< Value: {self.value} | Data: {self.data} | Left: {self.left} | Right: {self.right} >'

class BinaryTree:
    """This is a class method that creates a binary tree. The tree can be initialized without
    any input, or with an iterable.
    Running the insert method will filter down the tree recursively to find the spot that the
    node belongs (corresponding to value).
    """
    def __init__(self, iterable=None):
        self.root = None
        if iterable is not None:
            for i in iterable:
                self.insert(i)

    def __str__(self):
        return f'Root: {self.root} | Tree in order: {self.in_order}'

    def __repr__(self):
        return f'<In_order: {self.in_order} | Pre_order: {self.pre_order} | Post_order: {self.post_order}'

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        def _walk(current_node, value):
            if current_node.value > value:
                if current_node.left is None:
                    current_node.left = Node(value)
                    return True
                _walk(current_node.left, value)
            elif current_node.value < value:
                if current_node.right is None:
                    current_node.right = Node(value)
                    return True
                _walk(current_node.right, value)
            else:
                return False

        bool_success = _walk(self.root, value)
        print(bool_success)
        return bool_success



    def in_order(self, callable=lambda node: print(node.value)):
        """Go left: visit, visit, go right: visit
        """
        tree_list = []
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # visit
            tree_list.append(node.value)
            # callable(node)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)
        return tree_list

    def pre_order(self, callable=lambda node: print(node.value)):
        """visit, go left go right
        """
        tree_list = []
        def _walk(node=None):
            if node is None:
                return

            # Visit
            # callable(node)
            tree_list.append(node.value)
            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)
        return tree_list

    def post_order(self, callable=lambda node: print(node.value)):
        """go left, go right, visit
        """
        tree_list = []
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

            # Visit
            tree_list.append(node.value)
            # callable(node)

        _walk(self.root)
        return tree_list


