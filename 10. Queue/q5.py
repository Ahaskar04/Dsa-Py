class Node:
    def __init__(self, value, animal):
        self.value = value
        self.next = None 
        self.animal = animal
        
class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.length = 0
        
    def append(self, value, animal):
        newNode = Node(value, animal)
        if self.length == 0:
            self.head = newNode 
            self.tail = newNode 
            self.length += 1
            
        else:
            self.tail.next = newNode 
            self.tail = newNode 
                
    def popTopChoice(self, choice):
        if self.head is None:
            return "No animals"
    
        current = self.head
        prev = None
    
        while current:
            if current.animal == choice:
                if prev is None:
                    # First node matches
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
    
                self.length -= 1
                return current.value  # return animal value (e.g., name or ID)
            
            prev = current
            current = current.next
    
        # If no matching animal found
        return "No Dogs" if choice == 1 else "No Cats"
    def popTop(self):
        if self.head is None:
            return "No animals"
    
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None  # list is now empty
    
        self.length -= 1
        return removed_node.value
    
            
class AnimalShelterQueue:
    def __init__(self):
        self.animals = LinkedList()

    def enqueue(self, name, animal_type):
        """
        animal_type: 1 = Dog, 2 = Cat
        """
        self.animals.append(name, animal_type)

    def dequeue_any(self):
        return self.animals.popTop()

    def dequeue_dog(self):
        return self.animals.popTopChoice(1)

    def dequeue_cat(self):
        return self.animals.popTopChoice(2)

    def __str__(self):
        current = self.animals.head
        values = []
        while current:
            animal = "Dog" if current.animal == 1 else "Cat"
            values.append(f"{current.value} ({animal})")
            current = current.next
        return " -> ".join(values) if values else "No animals"