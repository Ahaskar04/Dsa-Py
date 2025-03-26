# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creation of Singly Linked List
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

#Insert element at end of linked list
class LinkedList:
    def __init__(self, value):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head == None:  # if linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #the last node's next value will point to the new node
            self.tail = new_node
        self.length += 1
        return self

#Print linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value) 
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
#Insert element at start of linked list
    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:  # if linked list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return self
    
#Insert element at given index of linked list
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

#Traversal of linked list
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
        
#search element in linked list
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1
    
#get method
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
#Set method: to update value of node at given index
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        return True
    
#pop first element
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            self.tail = None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
#pop last element
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
    
#remove element at given index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop_last()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
            return popped_node

#Delete all elements
    def deleteall(self):
        self.head = None
        self.tail = None
        self.length = 0