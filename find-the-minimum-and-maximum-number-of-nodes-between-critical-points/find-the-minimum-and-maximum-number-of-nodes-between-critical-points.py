# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head.val
        head = head.next
        if not head.next: return [-1, -1]
        
        first, last, currmin, curr = None, None, float("inf"), 1
        ahead = head.next
        while ahead:
            if prev > head.val < ahead.val or prev < head.val > ahead.val:
                if first is None: first = last = curr
                else:
                    currmin = min(currmin, curr - last)
                    last = curr
            prev, curr = head.val, curr + 1
            head, ahead = head.next, ahead.next
        
        return [currmin, last - first] if first and last and currmin != float("inf") else [-1, -1]