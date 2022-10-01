class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        sub = (int(correct[:2])*60 + int(correct[3:])) - (int(current[:2])*60 + int(current[3:]))
        op, res = (60, 15, 5, 1), 0        
        for o in op:
            res = res + ((sub) // o)
            sub = sub % o
        return res