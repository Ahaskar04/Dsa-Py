# Check if a Circular Linked List is Sorted
# Implement a function to check if the circular linked list is sorted in ascending order.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        if self.head is None or self.head.next == self.head:
            return True  # Empty or single-node list is trivially sorted
    
        temp = self.head
        while temp.next != self.head:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
        return True

            
        