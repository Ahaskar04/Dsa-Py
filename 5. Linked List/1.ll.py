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
        
