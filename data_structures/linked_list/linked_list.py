from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self, ):
        try:
            self.head: Node = None
            self._length: int = 0
        except TypeError:
            return TypeError

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def insert(self, val: Any) -> Any:
        prev_node = self.head
        self.head = Node(val, prev_node)
        self._length += 1

    def includes(self, val) -> bool:
        current = self.head
        while current is not None:
            if current.val is val:
                return True
            current = current.next
        return False


# def small_list():
#     ll = LinkedList()
#     ll.insert(1)
#     ll.insert(2)
#     ll.insert(3)
#     ll.insert(4)
#     small_list_includes(ll)


# def small_list_includes(link_list):
#     some_bool = link_list.includes(3)
#     print(some_bool)


# if __name__ == '__main__':
#     small_list()


