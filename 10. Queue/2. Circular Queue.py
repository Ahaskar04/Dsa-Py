class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        value = [str(x) for x in self.items]
        return "Queue: " + str(value)

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def enqueue(self, item):
        if self.isFull():
            print("Queue is full")
            return
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
        self.items[self.top] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        item = self.items[self.start]
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start + 1 == self.maxSize:
                self.start = 0  
        else:
            self.start += 1
        return item
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.items[self.start]
    
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1