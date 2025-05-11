#Double Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.data)
            if temp_node.next   is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def transverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        def reverse_transverse(self):
            current_node = self.tail
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.prev

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

        def search(self, data):
            current_node = self.head
            while current_node is not None:
                if current_node.data == data:
                    return current_node
                current_node = current_node.next
            return None
        
        def get(self, index):
            if index <self.length  // 2:
                current_node = self.head
                for _ in range(index):
                    current_node = current_node.next
            else:
                current_node = self.tail
                for _ in range(self.length - 1, index, - 1):
                    current_node = current_node.prev
            return current_node
        
        def set(self, index, data):
            node = self.get(index)
            if node:
                node.data = data
            else:
                raise IndexError("Index out of bounds")
            
        def insert(self, index, data):
            new_node = Node(data)
            temp_node = self.head
            if index == 0:
                self.prepend(data)
            elif index == self.length:
                self.append(data)
            elif index < 0 or index > self.length:
                raise IndexError("Index out of bounds")
            else:
                for _ in range(index - 1):
                    temp_node = temp_node.next
                new_node.next = temp_node.next
                new_node.prev = temp_node
                temp_node.next.prev = new_node
                temp_node.next = new_node
                self.length += 1

            def pop_first(self):
                if self.head is None:
                    return None
                popped_node = self.head
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                else:
                    self.tail = None
                self.length -= 1
                return popped_node.data
            
            def pop(self):
                if self.tail is None:
                    return None
                popped_node = self.tail
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.next = None
                else:
                    self.head = None
                self.length -= 1
                return popped_node.data
            
            def remove(self, data):
                current_node = self.head
                while current_node is not None:
                    if current_node.data == data:
                        if current_node.prev is not None:
                            current_node.prev.next = current_node.next
                        else:
                            self.head = current_node.next
                        if current_node.next is not None:
                            current_node.next.prev = current_node.prev
                        else:
                            self.tail = current_node.prev
                        self.length -= 1
                        return True
                    current_node = current_node.next
                return False