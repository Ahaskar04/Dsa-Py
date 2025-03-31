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
            
        