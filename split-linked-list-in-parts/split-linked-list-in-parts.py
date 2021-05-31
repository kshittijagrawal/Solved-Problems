# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        length, curr = 0, root
        while curr:
            length += 1
            curr = curr.next
        
        each, buffer = length//k, length%k
        res, curr = [], root
        
        while k>0:
            head, iterations = ListNode(0), each+1 if buffer>0 else each
            headcurr = head
            
            for i in range(iterations):
                headcurr.next = ListNode(curr.val)
                headcurr, curr = headcurr.next, curr.next
            buffer, k = buffer-1, k-1
            res.append(head.next)
            
        return res