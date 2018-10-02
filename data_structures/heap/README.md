# Hash Table

# By Max McFarland

# Purpose
This data structure is meant to show the functionality of a hand built hash table. Using a pre-built hashing key, this table will create a list with 8192 indices. A piece of data can be stored in this list using a key. This allows for an O(1) lookup time, since we can get the the exact index of where the data is stored in the list.

# Using the Table
To start a new table, simply create a new HashTable instance by calling the hash table class. The table has three methods, set(), get(), and remove(). All values are stored in a linked list within the table to prevent collosion problems.
- The set() method takes in two arguments, a key and a value. The key must be short string representative of the data in some way, however the value can be of whatever type or length the user wants. Once passed in, the key will be hashed, then used to store the value at the corresponding index of the hashtable.
- The get() method takes in only one argument, the key. Once a key is passed into the method, it is hashed and used to lookup the corresponding index in the hash table.
- The remove() method also takes in only one argument, the key. Once a key is passed into the method, it is hashed, used to lookup the corresponding index. The value at that index is returned, then deleted from the hash table.
All of these methods are an O(1) time constraint except for the get() method, which is O(k/n), where n is the total number of indicies in the hash table and k is the length of the linked list stored in the given index.

# Testing
To test the functionality of the stack and queue methods, pytest needs to be installed in your virtual environment. This can be done using pip, or any other virtual environment module. Running pytest will run the various tests that have been written to test the functionality of the hash table. Most of the tests utilize the error handling built into the table.
