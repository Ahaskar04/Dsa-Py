# Insertion at the End of a Singly Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
        
    def create(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        return self
        
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    # Implement Here        
    def append(self, value):
        new_node = Node(value)
        if (self.head == None):
            self.head = new_node
            self.tail = new_node
            new_node.next == None
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self
        
    def print(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
        
ll = LinkedList()
ll.create(20)
print(ll.print())
ll.prepend(10)
print(ll.print())
ll.append(30)
print(ll.print())