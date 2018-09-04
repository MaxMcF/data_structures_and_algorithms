from node import Node

class Stack:

    def __init__(self, vals=None):
        """This creates a new Stack, initializing it with a length of 0.
        If an iterable is passed in, the stack will push all of the corresponding values.
        """
        self.length = 0
        self.top = None
        if vals is not None:
            for i in vals:
                self.push(i)

    def __len__(self):
        return self.length

    def __str__(self):
        return f'Stack Top: {self.top} | Stack Length: {len(self)}'

    def push(self, value):
        """This method takes an input value and puts it ontop of the stack
        """
        self.top = Node(value, self.top)
        self.length += 1
        return self.top.val

    def pop(self):
        """This method finds the first value on the stack, and removes it.
        """
        if self.length < 1:
            raise ValueError
        temp = self.top
        self.top = self.top.next
        self.length -= 1
        return temp.val

    def peek(self):
        return self.top
