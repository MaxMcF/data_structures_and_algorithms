class Node:
    def __init__(self, val, data=None, left=None, right=None):
        self.value = val
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'Value: {self.value} | Data: {self.data}'
    def __repr__(self):
        pass

class BinaryTree:
    def __init__(self, iterable=None):
        self.root = None
        if iterable is not None:
            for i in iterable:
                self.insert(i)

    def __str__(self):
        return f'Root: {self.root} | '

    def __repr__(self):
        pass

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        def _walk(current_node, value):
            if current_node.value > value:
                if current_node.left is None:
                    current_node.left = Node(value)
                else:
                    _walk(current_node.left, value)
            else:
                if current_node.right is None:
                    current_node.right = Node(value)
                else:
                    _walk(current_node.right, value)

        _walk(self.root, value)


    def in_order(self, callable=lambda node: print(node.value)):
        """Go left: visit, visit, go right: visit
        """
        def _walk(node=None):
            if node is None:
                return

            # Go left
            if node.left is not None:
                _walk(node.left)

            # visit
            callable(node)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def pre_order(self, callable=lambda node: print(node.value)):
        """visit, go left go right
        """
        def _walk(node=None):
            if node is None:
                return

            # Visit
            callable(node)

            # Go left
            if node.left is not None:
                _walk(node.left)

            # Go right
            if node.right is not None:
                _walk(node.right)

        _walk(self.root)

    def post_order(self, callable=lambda node: print(node.value)):
        """go left, go right, visit
        """
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
            callable(node)

        _walk(self.root)

new_tree = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
new_tree.in_order()
