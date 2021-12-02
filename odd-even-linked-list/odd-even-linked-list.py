# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try: o, e = head, head.next
        except: return head
        
        conn = e
        while e and e.next:
            o.next = o.next.next
            e.next = e.next.next
            o = o.next
            e = e.next
        
        o.next = conn
        return head