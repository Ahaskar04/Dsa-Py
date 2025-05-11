# Write a function to delete a node from a singly linked list and return deleted_node. 
# The function should take the index(starting from 0) of the node to be deleted as a parameter.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def create(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        return self
       
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
        current = self.head
        if(index<0 or index >= self.length):
            return None
        else:
            for _ in range(index):
                current = current.next
            return current

    # Implement Here    
    def remove(self, index):
        if(index<0 or index >= self.length):
            return None
            
        if(index ==0 ):
            next_node = self.get(index+1)
            deleted_node = self.head
            self.head = next_node
            deleted_node.next = None
            self.length -= 1
            return deleted_node
            
        deleted_node = self.get(index)
        previous_node = self.get(index-1)
        next_node = self.get(index+1)
        previous_node.next = next_node
        
        if index == self.length - 1:  # Deleting the tail
            self.tail = previous_node
        
        deleted_node.next = None
        self.length -= 1
        return deleted_node
            
            
            
ll = LinkedList()
ll.create(20)
print(ll.print())
ll.prepend(10)
print(ll.print())
ll.append(30)
print(ll.print())
ll.remove(2)
print(ll.print())