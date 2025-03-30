
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def get(self, index):
        current = self.head
        if (index < 0 or index >= self.length ):
            return None
        else:
            for _ in range(index):
                current = current.next
        return current
    
    # def find_middle(self):
    #      TODO
    #     mid_index = self.length // 2
    #     return self.get(mid_index)


# "fast and slow pointer" technique
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

