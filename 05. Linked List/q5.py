# Write a function to reverse a singly linked list. The function should reverse the original linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def get(self, index):
        node = self.head3
        if (index<0 or self.length < index):
            return None
        else:
            for _ in range(index):
                node = node.next
        return node.value
        
    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head  # Update tail to old head
    
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
    
        self.head = prev  # Update head to new front node
