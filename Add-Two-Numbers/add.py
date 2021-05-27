# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        first, second = l1, l2
        carry = 0
        res = ListNode(0)
        res_curr = res
        while first and second:
            _sum = first.val + second.val + carry
            carry = _sum//10
            res_curr.next = ListNode(_sum%10)
            first = first.next
            second = second.next
            res_curr = res_curr.next
            
        tocompute = first if first is not None else second
        while tocompute:
            _sum = tocompute.val + carry
            carry = _sum//10
            res_curr.next = ListNode(_sum%10)
            tocompute = tocompute.next
            res_curr = res_curr.next
        if carry == 0:
            return res.next
        res_curr.next = ListNode(carry)
        return res.next