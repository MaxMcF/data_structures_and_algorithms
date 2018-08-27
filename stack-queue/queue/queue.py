from node import Node

class Queue:

    def __init__(self, vals=None):
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
        self.back = Node(value, self.back)
        self.length += 1
        if self.length == 1:
            self.front = self.back
        return self.back.val

    def dequeue(self):
        current = self.back
        while current.next is not self.front:
            current = current.next
        temp = current.next
        current.next = None
        self.front = current
        return temp.val
