# This code implements a stack using a singly linked list.
# It includes methods to push, pop, and find the minimum element in the stack.


# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creation of Singly Linked List
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.value = value
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:  
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return self

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value) 
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:  
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
    
    def pop_last(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            for _ in range(self.length-2):
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return popped_node.value
        
    def min(self):
        if self.head is None:
            return None
        min_node = self.head
        current = self.head
        while current:
            if current.value < min_node.value:
                min_node = current
            current = current.next
        return min_node.value

    
class Stack:
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def push(self, value):
        self.linked_list.append(value)

    def pop(self):
        self.linked_list.pop_last()
        
    def min(self):
        return self.linked_list.min()
        
ll = LinkedList(10)
stack = Stack(ll)
stack.push(5)
stack.push(20)
stack.push(3)
print(stack.linked_list)        # 10 -> 5 -> 20 -> 3
print("Min:", stack.min())      # Min: 3
stack.pop()
print(stack.linked_list)        # 10 -> 5 -> 20
print("Min:", stack.min())      # Min: 5
   