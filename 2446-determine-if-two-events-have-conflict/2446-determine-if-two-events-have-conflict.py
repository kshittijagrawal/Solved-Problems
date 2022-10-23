class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2
        
        if end1 < start2 or end2 < start1:
            return False
        else:
            return True