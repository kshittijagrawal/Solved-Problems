# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head, left, right):
        if head.next is None or left == right:
            return head
        
        dummy = dcurr = ListNode(0)
        dummy.next = head
        for _ in range(left-1):
            dcurr = dcurr.next
            
        prev, curr, s = None, dcurr.next, dcurr.next
        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        
        dcurr.next = prev
        s.next = curr
        return dummy.next