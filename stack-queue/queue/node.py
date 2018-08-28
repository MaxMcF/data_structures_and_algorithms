class Node:
    def __init__(self, value, _next):
        self.val = value
        self.next = _next

    def __repr__(self):
        return f'< Value: {self.val} | Next: {self.next.val} >'
