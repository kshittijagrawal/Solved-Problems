class Solution:
    def reverseVowels(self, s: str) -> str:
        lo, hi = 0, len(s) - 1
        c = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        res = [ch for ch in s]
        
        while lo < hi:
            
            while lo < hi and s[lo] not in c:
                lo += 1
            
            while lo < hi and s[hi] not in c:
                hi -= 1
            
            res[lo], res[hi] = s[hi], s[lo]
            lo, hi = lo + 1, hi - 1
        
        return "".join(res)
            
            