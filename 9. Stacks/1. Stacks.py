# LIFO Stack

class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def delete(self):
           self.items = None      