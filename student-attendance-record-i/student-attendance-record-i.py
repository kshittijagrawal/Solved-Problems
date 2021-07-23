class Solution:
    def checkRecord(self, s: str) -> bool:
        a, l, lflag = 0, 0, 0
        for c in s:
            if c == "L":
                l, lflag = l+1, 1
            else:
                lflag = l = 0
                if c == "A": a += 1
            if l == 3 and lflag == 1: return False
        return True if a < 2 else False
                