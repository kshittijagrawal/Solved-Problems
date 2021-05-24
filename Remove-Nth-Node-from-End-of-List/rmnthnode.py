# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
            
        remove = length - n
        if remove == 0:
            return head.next
        
        count, current = 1, head
        while True:
            if count == remove or count == length-1:
                current.next = current.next.next
                break
            count += 1
            current = current.next
            
        return head