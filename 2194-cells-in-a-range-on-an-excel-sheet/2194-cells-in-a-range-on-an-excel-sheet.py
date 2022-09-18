class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        sc, ec = s[0], s[3]
        sr, er = int(s[1]), int(s[4])
        res = []
        
        for i in range(ord(sc), ord(ec) + 1):
            for j in range(sr, er + 1):
                res.append(chr(i) + str(j))
                
        return res
        
        
        