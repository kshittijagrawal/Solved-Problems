class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        if s == t or length == 0:
            return True
        
        for i in range(len(t)-1, -1, -1):
            if t[i] == s[length-1]:
                length -= 1
                
            if length <= 0:
                return True
                
        return False