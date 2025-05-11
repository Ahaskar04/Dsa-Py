# Remove Duplicates from a Singly Linked List


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
        
    def delete(self, index):
        if index < 0 or index >= self.length:
            return  # or raise an exception
        if index == 0:
            self.head = self.head.next
            if self.length == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            to_delete = prev.next
            prev.next = to_delete.next
            if index == self.length - 1:
                self.tail = prev
        self.length -= 1

    
    # def remove_duplicates(self):
    #     current = self.head
    #     prev = None
    #     seen = set()
    #     while current:
    #         if current.value in seen:
    #             prev.next = current.next
    #             self.length -= 1
    #             if current == self.tail:
    #                 self.tail = prev
    #         else:
    #             seen.add(current.value)
    #             prev = current
    #         current = current.next



def remove_duplicates(self):
    if self.head is None:
        return
    node_values = set()  # set to store unique node values
    current_node = self.head
    node_values.add(current_node.value)
    while current_node.next:
        if current_node.next.value in node_values:  # duplicate found
            current_node.next = current_node.next.next
            self.length -= 1
        else:
            node_values.add(current_node.next.value)
            current_node = current_node.next
    self.tail = current_node