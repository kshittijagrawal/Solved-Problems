class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = collections.Counter(s)        
        for c in t:
            if c not in scount:
                return False
            scount[c] -= 1
            if scount[c] <= 0:
                del scount[c]
        
        return True if not scount else False