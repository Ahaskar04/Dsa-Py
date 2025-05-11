#  Intersection

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def intersection(llA, llB):
        if llA.tail != llB.tail:
            return None

        lenA = llA.length
        lenB = llB.length

        diff = abs(lenA - lenB)

        if lenA > lenB:
            longer = llA.head
            shorter = llB.head
        else:
            longer = llB.head
            shorter = llA.head

        for _ in range(diff):
            longer = longer.next

        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next

        return None