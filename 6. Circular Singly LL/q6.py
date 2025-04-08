# Check if a Circular Linked List is Sorted
# Implement a function to check if the circular linked list is sorted in ascending order.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        newNode = Node(data)
    
        # Case 1: Empty list
        if self.head is None:
            self.head = newNode 
            newNode.next = newNode
            return
    
        # Case 2: Insert before head
        if data < self.head.data:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newNode
            newNode.next = self.head
            self.head = newNode
            return
    
        # Case 3: Insert somewhere after head
        prev = self.head
        current = self.head.next
        while current != self.head and current.data < data:
            prev = current
            current = current.next
    
        prev.next = newNode
        newNode.next = current
    
                    
            
            
            
            
            
            
        