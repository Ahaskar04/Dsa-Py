class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        values = [str(x.value) for x in self]
        return '\n'.join(values)
    
    def is_empty(self):
        if self.linkedList.head == None:
            return True
    
    def push(self, item):
        newNode = Node(item)
        newNode.next = self.linkedList.head
        self.linkedList.head = newNode

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        poppedNode = self.linkedList.head.value
        self.linkedList.head = self.linkedList.head.next
        self.size -= 1
        return poppedNode
        
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.linkedList.head.value