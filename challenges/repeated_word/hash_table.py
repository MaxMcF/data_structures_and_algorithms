
from typing import Any

class Node:
    def __init__(self, key, val, _next):
        self.key = key
        self.val = val
        self.next = _next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Next: {self.next}>'

class LinkedList(object):
    def __init__(self, initial_data=None, tuple_data=None):
        """This initializes the linked list object by creating a node for each value inputed.

            ARGS:
                Initial data can be either a list, or a single piece of data.
                Tuple data can also be either a list, or a single piece of data.
        """
        try:
            self.head: Node = None
            self._length: int = 0
            if initial_data is not None:
                try:
                    for item in initial_data:
                        self.insert(item)
                except:
                    self.insert(initial_data)
            if tuple_data is not None:
                try:
                    for item in tuple_data:
                        self.insert(item)
                except:
                    self.insert(tuple_data)
        except TypeError:
            return TypeError

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def insert(self, key, val: Any) -> Any:
        '''Creates a new node and appends it to the beginning of the list
            This is done by re-stating which node is the head(the one youre appending)
            then setting the previous head equal to the next value of the appended item
        '''
        self.head = Node(key, val, self.head)
        self._length += 1

    def includes(self, key) -> bool:
        '''Checks to see if a value is contained in the list by iterating through and
        checking every node against the input value. If the value exists in the list
        , the function will return true if it does not exist in the list, it will return false.
        '''
        current = self.head
        while current is not None:
            if current.key is key:
                return True
            current = current.next
        return False

    def append(self, val, key=None) -> bool:
        '''Creates a new node and appends it at the end of the linked list
        '''
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(key, val, None)
        return True

    def insert_before(self, val, target_val) -> bool:
        '''Creates a new node and appends it before the target value
            args:
                new Node value, target Node value to insert before
            returns:
                True if the node was inserted
                False if the target value is not in the SLL
        '''
        current = self.head
        while current.next.val is not target_val:
            current = current.next
            if current.next == None:
                return False
        current.next = Node(val, current.next)
        return True

    def insert_after(self, val, target_val) -> bool:
        '''Creates a new node and appends it after the target value
        '''
        current = self.head
        while current.val is not target_val:
            current = current.next
            if current == None:
                return False
        current.next = Node(val, current.next)
        return True

    def find_k(self, k) ->bool:
        '''Takes in an input value of K, which corresponds to that
        many indexes from the end of the list. This function takes in the input,
        and returns the value of the item at index of length - k.
        '''
        if k < 0:
            raise IndexError
        tortoise = self.head
        hare = self.head
        for i in range(k):
            if hare is not None:
                hare = hare.next
            else:
                raise IndexError
        while hare.next is not None:
            hare = hare.next
            tortoise = tortoise.next
        return tortoise.val

class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [None] * self.table_size

    def __repr__(self):
        pass

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        if self.hashtable[self._hash_key(key)] is None:
            self.hashtable[self._hash_key(key)] = LinkedList()
            self.hashtable[self._hash_key(key)].insert(key, value)
            self.entries_count += 1
            return True
        if self.hashtable[self._hash_key(key)].includes(key):
            raise TypeError
        self.hashtable[self._hash_key(key)].insert(key, value)
        self.entries_count += 1
        return False

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """

        linked_list = self.hashtable[self._hash_key(key)]
        if linked_list is None:
            raise TypeError
        if linked_list.head is None:
            raise TypeError
        temp = linked_list.head
        while linked_list:
            if linked_list.head.key is key:
                return linked_list.head.val
            linked_list.head = linked_list.head.next
        linked_list.head = temp
        raise TypeError


    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        ll = self.hashtable[self._hash_key(key)]
        if ll is None:
            raise TypeError
        temp = ll.head
        if ll.head.key is key:
            temp = ll.head
            ll.head = ll.head.next
            return temp.val
        while ll:
            if ll.head.next.key is key:
                temp = ll.head.next
                ll.head.next = ll.head.next.next
                return temp.val
        if ll.head is None:
            self.hashtable[self._hash_key(key)] = None
        raise TypeError

