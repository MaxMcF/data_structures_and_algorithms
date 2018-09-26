from .linked_list import LinkedList

class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = []

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
            ll = LinkedList()
            self.hashtable[self._hash_key(key)] = ll.append(value, key)
            self.entries_count += 1
            return True
        self.hashtable[self._hash_key(key)].append(value, key)
        self.entries_count += 1
        return False

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        ll = self.hashtable[self._hash_key(key)]
        if ll is None:
            raise TypeError
        temp = ll.head
        while ll:
            if ll.head.key is key:
                return ll.head.key
            ll.head = ll.head.next
        ll.head = temp
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
