class Solution:
    def evalRPN(self, tokens):
        stack = Stack() 
        for token in tokens:
            process_token(stack, token)
        return stack.pop()

def perform_operation(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a // b if a * b > 0 else -(abs(a) // abs(b))



def is_operator(token):
    return token in "+-*/"


def process_token(stack, token):
    if is_operator(token):
        b = stack.pop()
        a = stack.pop()
        result = perform_operation(a, b, token)
        stack.push(result)  
    else:
        stack.push(int(token)) 


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.height = 0

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            raise IndexError("Pop from an empty stack")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp.value