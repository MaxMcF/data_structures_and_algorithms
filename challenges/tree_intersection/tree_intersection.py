
from ..data_structures.hash_table import Hashtable()


def tree_intersection(tree_one, tree_two):
    return_list = []
    tree_hash_table = Hashtable()
    def _walk(node):
        tree_hash_table.set(node.value, node.value)
        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)
    _walk(tree_one.root)
    def _check_tree(node):
        common = tree_hash_table.get(node.value)
        if common:
            return_list.append(common)
        if node.left:
            _check_tree(node.left)
        if node.right:
            _check_tree(node.right)
    _check_tree(tree_two.root)
    return return_list
