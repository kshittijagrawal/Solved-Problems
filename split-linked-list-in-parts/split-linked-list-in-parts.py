# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        parts, extras = length // k, length % k
        res = []
        while head:
            curr, prev = head, head
            
            for i in range(parts + bool(extras)):
                if i: prev = prev.next
                head = head.next
                
            extras, prev.next, k = extras - 1, None, k - 1
            if extras < 0: extras = 0
            res.append(curr)

        for _ in range(k): res.append(None)
        return res