# Write a code in the language of your choice to implement a singly linked list.

class linkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def create(self, value):
        new_node = linkedList(value)
        self.next = new_node
        self.tail = new_node
        return new_node
