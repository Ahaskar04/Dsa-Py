class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        if temp_node is not None:
            while True:
                result += str(temp_node.data)
                if temp_node.next == self.head:
                    break
                result += ' <-> '
                temp_node = temp_node.next
        return result
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse_forward(self):
        temp_node = self.head
        if temp_node is not None:
            while True:
                print(temp_node.data, end=' ')
                if temp_node.next == self.head:
                    break
                temp_node = temp_node.next
        print()

    def traverse_backward(self):
        temp_node = self.tail
        if temp_node is not None:
            while True:
                print(temp_node.data, end=' ')
                if temp_node.prev == self.tail:
                    break
                temp_node = temp_node.prev
        print()

    def search(self, key):
        temp_node = self.head
        if temp_node is not None:
            while True:
                if temp_node.data == key:
                    return temp_node
                if temp_node.next == self.head:
                    break
                temp_node = temp_node.next
        return None
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node.data