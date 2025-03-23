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

    