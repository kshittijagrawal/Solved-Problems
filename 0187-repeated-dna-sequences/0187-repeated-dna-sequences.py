class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s) < 10:
            return res
        
        c = {}
        for i in range(len(s) - 9):
            dna = s[i:i+10]
            c[dna] = c.get(dna, 0) + 1
        
        for key in c:
            if c[key] > 1:
                res.append(key)
        
        return res
            