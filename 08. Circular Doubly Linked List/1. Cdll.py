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
        current_index = None
        if index < self.length // 2:
            current_index = self.head
            for i in range(index):
                current_index = current_index.next
        else:
            current_index = self.tail
            for i in range(self.length - 1, index, -1):
                current_index = current_index.prev
            return current_index
        
    def set(self, index, data):
        temp = self.get(index)
        if temp is not None:
            temp.data = data
            return True
        else:
            return False
        
    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            self.prepend(data)
        elif index == self.length:
            self.append(data)
        else:
            new_node = Node(data)
            temp_node = self.get(index-1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
            self.length += 1

    def pop_first(self):
            popped_node = self.head
            if self.head is None:
                return None
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                popped_node.next.prev = self.tail
                popped_node.prev.next = self.head
                self.head.prev = self.tail
                self.tail.next = self.head
                self.length -= 1
            return popped_node.data
        
    def pop(self):
            popped_node = self.tail
            if self.head is None:
                return None
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                popped_node.prev.next = self.head
                popped_node.next.prev = self.tail
                self.head.prev = self.tail
                self.tail.next = self.head
                self.length -= 1
            return popped_node.data
        
    def remove(self, key):
        if self.head is None:
            return False
        if self.head.data == key:
            self.pop_first()
            return True
        elif self.tail.data == key:
            self.pop()
            return True
        else:
            temp_node = self.head
            while True:
                if temp_node.data == key:
                    temp_node.prev.next = temp_node.next
                    temp_node.next.prev = temp_node.prev
                    self.length -= 1
                    return True
                if temp_node.next == self.head:
                    break
                temp_node = temp_node.next
        return False
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0