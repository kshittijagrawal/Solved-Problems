# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        length, curr = 0, head
        while curr:
            length += 1
            curr = curr.next
        
        front, back = k, length-k+1
        if front >= back: front, back = back, front
        if front == back:
            return head
        
        prevf, currf, prevb, currb = None, None, None, None
        count, curr = 1, head
        while 1:
            if count == front-1:
                prevf, currf = curr, curr.next
            if count == back-1:
                prevb, currb = curr, curr.next
                break
            count, curr = count + 1, curr.next
        
        if prevf is None:           # for swapping head and tail node
            if head is prevb:
                prevb.next, currb.next = currb.next, prevb
                head = currb
            else:
                curr = head
                curr.next, currb.next = None, curr.next
                prevb.next = curr
                head = currb
            
        elif front == back-1:       # for swapping consecutive nodes
            currf.next, currb.next = currb.next, currf
            prevf.next = currb
            
        else:                       # in all other cases
            currf.next, currb.next = currb.next, currf.next
            prevf.next, prevb.next = currb, currf
            
        return head
        
        