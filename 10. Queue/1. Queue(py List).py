#FIFO

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        value = [str(x) for x in self.items]
        return "Queue: " + str(value)

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(0, item)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.isEmpty():
            return None
        return self.items[-1]
    
    def delete(self):
        self.items = []