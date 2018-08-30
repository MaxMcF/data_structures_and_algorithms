from stack import Stack
from node import Node


def multi_bracket_validation(input_string):
    stack = Stack()
    for item in input_string:
        if item in ('{', '[', '(', ')', ']', '}'):
            if item is ')':
                top = stack.peek()
                if top is None:
                    stack.push(item)
                elif top.val is '(':
                    stack.pop()
                else:
                    return False
            elif item is '}':
                top = stack.peek()
                if top is None:
                    stack.push(item)
                elif top.val == '{':
                    stack.pop()
                else:
                    return False
            elif item is ']':
                top = stack.peek()
                if top is None:
                    stack.push(item)
                elif top.val is '[':
                    stack.pop()
                else:
                    return False
            else:
                stack.push(item)
    check_val = stack.peek()
    if check_val is not None:
        return False
    else:
        return True


actual = multi_bracket_validation('}}')
print(actual)
