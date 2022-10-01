class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        initial = int(current[:2])*60 + int(current[3:])
        final = int(correct[:2])*60 + int(correct[3:])
        sub = final - initial
        op = (60, 15, 5, 1)
        res = 0
        
        for o in op:
            res = res + ((sub) // o)
            sub = sub % o
        return res