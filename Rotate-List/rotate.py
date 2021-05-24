# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if head is None:
            return head
            
        length = 0
        current = head
        while current.next:
            length += 1
            current = current.next
        length = length+1
        
        rotations = k % length
        if rotations == 0:
            return head
        
        first_half_length =  length - rotations
        count, first = 1, head
        while count < first_half_length:
            count += 1
            first = first.next
        second = first.next
        first.next = None
        current.next = head
        return second