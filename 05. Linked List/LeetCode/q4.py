# Given the head of a singly linked list, reverse the list, and return the reversed list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head  # Use parameter, not self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev  # Return the new head of the reversed list
