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
        first.next, second.next, head = second.next, first, second
        if first.next is None or first.next.next is None:
            return head
        
        prev, curr = first, first.next
        while curr and curr.next:
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = curr
            prev, curr = prev.next.next, curr.next
        
        return head