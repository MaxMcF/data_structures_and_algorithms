class Node:
    """This creates an animal instance
    """
    def __init__(self, _next, data, spec):
        self.next = _next
        self.tag = data
        self.cat_or_dog = spec

    def __repr__(self):
        return f'< Species: {self.spec} | Next: {self.next.spec} | Tag: {self.tag} >'


class AnimalShelter:
    """This is the Animal shelter linked list class, which allows a user to add
    animals by using the enqueue method, and adopt animals using the dequeue method.
    """
    def __init__(self):
        self.tags = 0

    def __len__(self):
        return self.tags

    def enqueue(self, spec):
        self.tags += 1
        self.back = Node(self.back, self.tags, spec)
        if self.tags == 1:
            self.front = self.back
        return self.back.val

    def dequeue(self, prefrence):
        adopted = None
        while self.back is not None:
            if self.back.val == prefrence:
                adopted = self.back
                self.back = self.back.next
        return adopted
        print(stack.peek)
        while stack. is not prefrence:
            self.enqueue(stack.pop())
        adopted = stack.pop()
        while stack.peek is not None:
            self.enqueue(stack.pop())
        return adopted

# class dogs(AnimalShelter):
#     """
#     """
#     def __init__(self):
#         self.

