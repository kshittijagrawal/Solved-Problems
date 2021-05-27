# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = temp = list2
        while temp.next:
            temp = temp.next
        tail2 = temp
        
        count = 0
        temp = list1
        end1, start3 = None, None
        while temp:
            if count == a-1:
                end1 = temp
            if count == b+1:
                start3 = temp
                break
            temp = temp.next
            count += 1
        
        end1.next = head2
        tail2.next = start3
        return list1