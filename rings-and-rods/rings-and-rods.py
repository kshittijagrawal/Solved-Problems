class Solution:
    def countPoints(self, rings: str) -> int:
        c = {str(i): set() for i in range(10)}
        res = 0
        for i in range(1, len(rings), 2):
            c[rings[i]].add(rings[i-1])
        
        for i in range(10):
            if len(c[str(i)]) == 3:
                res += 1
        
        return res