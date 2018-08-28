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

class AnimalShelter:
    def __init__(self):
        self.length = 0
        self.front = None
        self.back = None

    def __len__(self):
        return self.length

    def enqueue(self, value):
        self.back = Node(value, self.back)
        self.length += 1
        if self.length == 1:
            self.front = self.back
        return self.back.val

    def dequeue(self, prefrence):
        stack = Stack()
        while self.back is not None:
            temp = self.back
            stack.push(temp)
            self.back = self.back.next
        print(stack.peek)
        while stack.peek.val is not prefrence:
            self.enqueue(stack.pop())
        adopted = stack.pop()
        while stack.peek is not None:
            self.enqueue(stack.pop())
        return adopted


