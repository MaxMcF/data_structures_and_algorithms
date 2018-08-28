class Node:
    def __init__(self, value, _next):
        self.val = value
        self.next = _next

    def __repr__(self):
        return f'< Value: {self.val} | Next: {self.next.val} >'

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

class Queue:
    def __init__(self):
        self.back = None
        self.front = None
        self.length = 0

    def enqueue(self, value):
        stack_one = Stack()
        stack_two = Stack()
        stack_one.push(value)
        current = self.back
        while current is not None:
            stack_one.push(current)
            current = current.next
        while stack_one.top is not None:
            item = stack_one.pop()
            stack_two.push(item)




