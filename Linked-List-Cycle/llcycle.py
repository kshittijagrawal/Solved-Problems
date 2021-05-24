# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        current = head
        while current:
            if current.val == "Seen":
                return True
            current.val = "Seen"
            current = current.next
        return False