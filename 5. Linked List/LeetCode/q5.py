# Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        # TODO
        word = ""
        current = head 
        while current:
            word += str(current.val)
            current = current.next
        tempWord = word[::-1]
        if word == tempWord:
            return True
        else:
            return False
            
# This is not the best solution as the same complexity can be achieved with O(n) time and O(1) space.
# The above solution has O(n) time and O(n) space complexity.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class Solution(object):
    def isPalindrome(self, head):
        #find te middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        #compare the first half and the reversed second half
        #head is the first half and prev is the reversed second half
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
    
