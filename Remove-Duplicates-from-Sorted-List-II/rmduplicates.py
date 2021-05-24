# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        
        flag = 0
        current = head
        while current.next:
            if current.val == current.next.val:
                flag = 1
                current.next = current.next.next
            else:
                if flag == 1:
                    current.val = "*"
                current = current.next
                flag = 0
        if flag == 1:
            current.val = "*"
        
        current = head
        while current and current.next:
            if current.next.val == "*":
                current.next = current.next.next
            else:
                current = current.next
        
        return head if head.val != "*" else head.next