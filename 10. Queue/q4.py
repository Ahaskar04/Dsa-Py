# This code implements a queue using two stacks. The queue supports enqueue and dequeue operations.
# It uses two stacks to reverse the order of elements when dequeuing, ensuring that the first element added is the first one removed (FIFO).



# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def pop_head(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

    def is_empty(self):
        return self.head is None

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, value):
        self.list.prepend(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.list.pop_head()
        
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.list.head.value

    def is_empty(self):
        return self.list.is_empty()

    def __str__(self):
        current = self.list.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return '\n'.join(values)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        
    def __str__(self):
        value = [str(x) for x in self.items]
        return "Queue: " + str(value)
        
    def enqueue(self, value):
        s1 = self.stack1
        s1.push(value)
        
    def dequeue(self):
        s1 = self.stack1
        s2 = self.stack2
        while s1.list.head and s1.list.head.next:
            s2.push(s1.peek())
            s1.pop()
        dequeued = s1.pop()  # store the bottom (front of queue)
        while not s2.is_empty():
            s1.push(s2.peek())
            s2.pop()
        return dequeued

            
q = Queue()

# Enqueue some elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

# Dequeue and print results
print(q.dequeue())  # Expected: 10
print(q.dequeue())  # Expected: 20

# Enqueue again
q.enqueue(40)

print(q.dequeue())  # Expected: 30
print(q.dequeue())  # Expected: 40

# Try to dequeue from empty queue
try:
    print(q.dequeue())  # Should raise Exception
except Exception as e:
    print("Error:", e)

            
        
        