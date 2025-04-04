# Delete a Node from a Circular Singly Linked List
# Implement a method in the CircularLinkedList class to delete a node by value.

# Delete a Node from a Circular Singly Linked List
# Implement a method in the CircularLinkedList class to delete a node by value.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
    
    def delete_by_value(self, value):
        if self.length == 0:
            return False  # Empty list
    
        prev = self.tail
        current = self.head
    
        for _ in range(self.length):
            if current.value == value:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                    if current == self.tail:
                        self.tail = prev
                self.length -= 1  # ✅ Only reduce length after deletion
                return True
            prev = current
            current = current.next
    
        return False  # Value not found

            
    
            
                