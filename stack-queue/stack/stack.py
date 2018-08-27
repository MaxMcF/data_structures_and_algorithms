from node import Node

class Stack:

    def __init__(self, vals=None):
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
        self.top = Node(value, self.top)
        self.length += 1
        return self.top.val

    def pop(self):
        temp = self.top
        self.top = self.top.next
        return temp.val

    def peek(self):
        return self.top
