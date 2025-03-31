# You are given the heads of two sorted linked lists list1 and list2. 
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.  


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def printList(self, temp):
        current = temp
        while current:
            print(current.val, end = '->')
            current = current.next
        
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
                current = current.next
            else:
                current.next = l2
                l2 = l2.next
                current = current.next
        
        current.next = l1 or l2
        return dummy.next
        

        
        