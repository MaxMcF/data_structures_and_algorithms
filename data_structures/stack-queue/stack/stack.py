from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __repr__(self):
        return ('< Top Node: {} | Stack Length: {} >').format(self.top, int(self._length))

    def __str__(self):
        return ('Top Value: {} | Stack Length: {}').format(self.top.value, int(self._length))


    def __len__(self):
        return int(self._length)

    def push(self, value):
        '''Method which accepts a value of any type and creates a new node in the stack instance.

            Args:
                value(object): Any

            Return: Node
        '''

        self.top = Node(value, self.top)
        self._length += 1
        return self.top

    def pop(self):
        '''Method which finds the top value of the stack and removes it.
            The next value in the stack becomes the new top.

            Return:
                Top value of the stack.
        '''
        temp_top_value = self.top
        self.top = temp_top_value.next
        self._length -= 1
        return temp_top_value.value

    def peek(self):
        '''Method that finds the top value and returns it without modifying anything.

            Return:
                Top value of the stack.
        '''
        return self.top.value
