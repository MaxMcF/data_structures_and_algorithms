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
        return self.top

    def pop(self):
        temp = self.top
        self.top = self.top.next
        self.length -= 1
        return temp

    def peek(self):
        return self.top

class Queue:
    def __init__(self):
        self.back = None
        self.front = None
        self.length = 0

    def enqueue(self, value):
        """This method takes in a value and puts the value at the back of a queue.
        Instead of doing this manually, this challenge required the use of stacks.
        """
        stack_one = Stack()
        stack_one.push(value)
        current = self.back
        while current is not None:
            stack_one.push(current)
            current = current.next
        self.front = stack_one.pop()
        self.back = self.front
        while stack_one.top is not None:
            item = stack_one.pop()
            self.back = Node(item.val, self.back)

    def dequeue(self):
        """This method queues the back of a given queue.
        Instead of doing this manually, this challenge required the use of stacks.
        """
        stack_one = Stack()
        current = self.back
        while current is not None:
            stack_one.push(current)
            current = current.next
        dequeued = stack_one.pop()
        self.front = stack_one.pop()
        self.back = self.front
        while stack_one.top is not None:
            item = stack_one.pop()
            self.back = Node(item.val, self.back)
        return dequeued.val







