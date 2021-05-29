# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None: return l2
        if l2 is None: return l1
        res = ListNode(0)
        rescurr, curr1, curr2 = res, l1, l2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                rescurr.next = ListNode(curr1.val)
                curr1 = curr1.next
            else:
                rescurr.next = ListNode(curr2.val)
                curr2 = curr2.next
            rescurr = rescurr.next
        
        toeval = curr1 if curr2 is None else curr2
        while toeval:
            rescurr.next = ListNode(toeval.val)
            rescurr, toeval = rescurr.next, toeval.next
        
        return res.next