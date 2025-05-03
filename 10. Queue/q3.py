# Implement a SetOfStacks class that implements a stack using multiple stacks.


# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_last(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            current = self.head
            for _ in range(self.length - 2):
                current = current.next
            current.next = None
            self.tail = current
        self.length -= 1
        return popped_node.value

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result)


# Stack using linked list
class Stack:
    def __init__(self, capacity):
        self.linked_list = LinkedList()
        self.capacity = capacity

    def push(self, value):
        if not self.is_full():
            self.linked_list.append(value)
        else:
            print("Stack is full")

    def pop(self):
        return self.linked_list.pop_last()

    def is_full(self):
        return self.linked_list.length == self.capacity

    def is_empty(self):
        return self.linked_list.length == 0

    def __str__(self):
        return str(self.linked_list)


# SetOfStacks
class SetOfStacks:
    def __init__(self, capacity_per_stack):
        self.capacity = capacity_per_stack
        self.stacks = [Stack(self.capacity)]

    def push(self, value):
        if self.stacks[-1].is_full():
            self.stacks.append(Stack(self.capacity))
        self.stacks[-1].push(value)

    def pop(self):
        while self.stacks and self.stacks[-1].is_empty():
            self.stacks.pop()
        if not self.stacks:
            return None
        return self.stacks[-1].pop()

    def __str__(self):
        result = []
        for i, stack in enumerate(self.stacks):
            result.append(f"Stack {i+1}: {stack}")
        return "\n".join(result)
        
        
        
sos = SetOfStacks(3)
sos.push(1)
sos.push(2)
sos.push(3)  # First stack is now full
print(sos)
sos.push(4)  # New stack created
sos.push(5)
print(sos)

