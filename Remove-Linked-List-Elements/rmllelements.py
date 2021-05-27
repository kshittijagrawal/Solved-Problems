# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        if head == None:
            return head
        
        current = head
        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head if head.val != val else head.next