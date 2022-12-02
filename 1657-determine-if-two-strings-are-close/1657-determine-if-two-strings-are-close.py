class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        sone, stwo = set(), set()
        cone, ctwo = {}, {}
        
        for c1, c2 in zip(word1, word2):
            cone[c1] = cone.get(c1, 0) + 1
            sone.add(c1)
            
            ctwo[c2] = ctwo.get(c2, 0) + 1
            stwo.add(c2)
        
        if sone == stwo and Counter(cone.values()) == Counter(ctwo.values()):
            return True
        return False