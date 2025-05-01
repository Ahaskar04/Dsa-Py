# Nth element from the end of a linked list

# length - n + 1 th element from statrt

from linkedlist import LinkedList:

def nfromlast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1