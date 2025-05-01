class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self): # for iteration
        current = self.head
        while current:
            yield current.data
            current = current.next
    
class Queue:
    def __init__(self):
        self.LinkedList = LinkedListQueue()

    def __str__(self):
        value = [str(x) for x in self.items]
        return "Queue: " + str(value)
    
    def enqueue(self, item):
        newNode = Node(item)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        return self.LinkedList.head is None
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next    
            return tempNode.data
        
    def peek(self):
        if self.isEmpty():
            return None
        return self.LinkedList.head.data
    
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

    