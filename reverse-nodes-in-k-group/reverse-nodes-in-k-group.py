# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(s, e):
            prev = None
            while s != e:
                _next = s.next
                s.next = prev
                prev, s = s, _next
            return prev
        
        arr = []
        count, start, end = 0, head, head
        while 1:
            if count == k:
                prev = reverse(start, end)
                start, count = end, 0
                arr.append(prev)
            elif end.next is None:
                if count == k-1:
                    prev = reverse(start, end.next)
                    arr.append(prev)
                else:
                    arr.append(start)
                break
            else:
                count, end = count+1, end.next
        
        if len(arr) == 1:
             return arr[0]
        res = arr[0]
        rescurr = res
        while rescurr.next:
            rescurr = rescurr.next
            
        for group in arr[1:-1]:
            rescurr.next = group
            while rescurr.next:
                rescurr = rescurr.next

        rescurr.next = arr[-1]
        return res