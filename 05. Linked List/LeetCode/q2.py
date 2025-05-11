"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well. 

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # TODO
        current = ListNode()
        current = head
        # set1 = set()
        while current and current.next:
            # for i in set1:
                if current.val == current.next.val:
                    current.next = current.next.next
                    # self.length -= 1
                else:
                    # set1 += head
                    current = current.next
        return head
                    