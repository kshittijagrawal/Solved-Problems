# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, nums: List[int]) -> int:
        snums, res = set(nums), 0
        while head:
            if head.val in snums and (head.next == None or head.next.val not in snums):
                res += 1
            head = head.next
        return res