# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        first, second = head, head.next
        first.next = second.next
        second.next = first
        head = second
        if first.next is None or first.next.next is None:
            return head
        
        prevf, currf = first, first.next
        while currf.next and currf.next.next:
            temp = currf.next.next
            prevf.next = currf.next
            currf.next.next = currf
            currf.next = temp
            prevf, currf = currf, currf.next
        
        if currf.next is None:
            return head
        prevf.next = currf.next
        currf.next.next = currf
        currf.next = None
        return head