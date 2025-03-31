"""Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head."""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        current = ListNode()  # dummy node
        current.next = head
        dummy = current

        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next  
            else:
                dummy = dummy.next  

        return current.next  
