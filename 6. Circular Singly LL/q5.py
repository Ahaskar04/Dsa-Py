# Split a Circular Linked List into Two Equal Halves
# Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list. 

# Split a Circular Linked List into Two Equal Halves
# Write a function to split the circular linked list into two equal halves. If the list has odd number of nodes, the extra node should go to the first list. 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def split_list(self):
        if self.head is None or self.length == 0:
            return None, None
    
        mid = (self.length + 1) // 2  # Extra node to first list if odd
        temp = self.head
    
        # First circular list
        first_head = None
        first_tail = None
    
        for _ in range(mid):
            new_node = Node(temp.value)
            if first_head is None:
                first_head = first_tail = new_node
            else:
                first_tail.next = new_node
                first_tail = new_node
            temp = temp.next
    
        first_tail.next = first_head  # Make it circular
    
        # Second circular list
        second_head = None
        second_tail = None
    
        for _ in range(self.length - mid):
            new_node = Node(temp.value)
            if second_head is None:
                second_head = second_tail = new_node
            else:
                second_tail.next = new_node
                second_tail = new_node
            temp = temp.next
    
        if second_tail:
            second_tail.next = second_head  # Make it circular
    
        return first_head, second_head
 


