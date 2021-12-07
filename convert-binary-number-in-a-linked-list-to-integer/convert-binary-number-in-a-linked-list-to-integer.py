# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def total_nodes(dummy):
            total = 0
            while dummy != None:
                total += 1
                dummy = dummy.next
            return total
            
        power = total_nodes(head) - 1
        num = 0
        while head != None:
            num += (head.val * (2**power))
            power -= 1
            head = head.next
        return num