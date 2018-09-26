class Node:
    def __init__(self, key, val, _next):
        self.key = key
        self.val = val
        self.next = _next

    def __str__(self):
        return f'{self.val}'

    def __repr__(self):
        return f'<Node | Val: {self.val} | Next: {self.next}>'
