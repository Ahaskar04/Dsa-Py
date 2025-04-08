# Josephus Circle using Circular Linked List
# Solve the Josephus problem using a circular linked list. 
# Implement a function that takes the number of people n and the step rate k and returns the position of the last person standing.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        temp = self.head
        if self.count_nodes() == 0:
            return False
        while (self.count_nodes() != 1):
            for i in range(step-1):
                temp = temp.next 
            self.delete_node(temp.data)
            temp = temp.next
        return f"Last person left standing: {temp.data}"
        
        
cll = CircularLinkedList()
for i in range(1, 8):  #7 people
    cll.append(i)

print(cll.josephus_circle(2))  

