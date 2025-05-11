# Write a function to remove duplicates from an unsorted linked list. 
# Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5


from linkedlist import LinkedList

def remove_duplicates(ll):
    current = ll.head
    prev = None
    seen = set()

    while current:
        if current.value in seen:
            prev.next = current.next
            ll.length -= 1
            if current == ll.tail:
                ll.tail = prev
        else:
            seen.add(current.value)
            prev = current
        current = current.next