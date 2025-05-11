# Write a code in the language of your choice to implement a singly linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def create(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
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
ll.create(10)
print(ll.print()) # 10
