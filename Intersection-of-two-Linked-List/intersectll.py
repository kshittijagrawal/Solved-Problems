# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        len1, len2 = 0, 0
        curr1, curr2 = headA, headB
        while curr1:
            len1 += 1
            curr1 = curr1.next
        while curr2:
            len2 += 1
            curr2 = curr2.next
        
        smaller = headA if len1 <= len2 else headB
        larger = headA if len1 > len2 else headB
        
        count = 0
        while count < abs(len1-len2):
            larger = larger.next
            count += 1
        
        while smaller.next:
            if larger is smaller:
                return larger
            if larger.next is smaller.next:
                return larger.next
            smaller, larger = smaller.next, larger.next
        return smaller if smaller is larger else None