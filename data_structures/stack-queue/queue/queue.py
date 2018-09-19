from node import Node

class Queue:

    def __init__(self, vals=None):
        """This creates a new Queue, initializing it with a length of 0.
        If an iterable is passed in, the queue will enqueue all of the corresponding values.
        """
        self.length = 0
        self.front = None
        self.back = None
        if vals is not None:
            for i in vals:
                self.enqueue(i)


    def __len__(self):
        return self.length

    def __str__(self):
        return f'Queue Front: {self.front.val} | Queue Back: {self.back.val} | Stack Length: {len(self)}'

    def enqueue(self, value):
        """This method puts a value into the queue using FIFO methodology
        """
        self.back = Node(value, self.back)
        self.length += 1
        if self.length == 1:
            self.front = self.back
        return self.back.val

    def dequeue(self):
        """This method takes a single value out of the queue using FIFO methodology
        """
        if self.length < 1:
            raise ValueError
        current = self.back
        while current.next is not self.front:
            current = current.next
        temp = current.next
        current.next = None
        self.front = current
        self.length -= 1
        return temp.val
