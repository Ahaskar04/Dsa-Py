# 1 Linked List for 3 stacks 

class Node:
    def __init__(self, value, stackNumber):
        self.value = value
        self.stackNumber = stackNumber
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self.length = 0
        self.a = None 
        self.b = None 
        self.c = None 
        
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value) 
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
        
    def append(self, value, stackNumber):
        newNode = Node(value, stackNumber)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode 
            self.tail = newNode
            
        self.length += 1    
        
        if stackNumber == 1:
            self.a = newNode
        elif stackNumber == 2:
            self.b = newNode
        elif stackNumber == 3:
            self.c = newNode
            
    def pop_last(self, Number):
        if self.length == 0:
            return
    
        current = self.head
        last_found = None
        last_found_prev = None
        prev = None
    
        while current:
            if current.stackNumber == Number:
                last_found = current
                last_found_prev = prev
            prev = current
            current = current.next
    
        if last_found is None:
            return  # No such node found
    
        # Remove node from list
        if last_found == self.head:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            last_found_prev.next = last_found.next
            if last_found == self.tail:
                self.tail = last_found_prev
    
        self.length -= 1
    
        # Update a, b, c to new top of the stack
        current = self.head
        new_top = None
        while current:
            if current.stackNumber == Number:
                new_top = current
            current = current.next
    
        if Number == 1:
            self.a = new_top
        elif Number == 2:
            self.b = new_top
        elif Number == 3:
            self.c = new_top

class Stack:
    def __init__(self, linked_list):
        self.linked_list = linked_list

    def push(self, value, stackNumber):
        self.linked_list.append(value, stackNumber)

    def pop(self, stackNumber):
        self.linked_list.pop_last(stackNumber)

    
    
    
    
ll = LinkedList()
ll.append(10, 1)
ll.append(20, 2)
ll.append(30, 1)
ll.append(40, 3)
ll.append(50, 1)
print(ll)

ll.pop_last(3)  # Should remove 50
print(ll)

# ll.pop_last(1)  # Should remove 30
# ll.pop_last(2)  # Should remove 20
