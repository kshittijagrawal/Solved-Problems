class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(1, len(s), 2):
            res = res + s[i-1] + chr(ord(s[i-1]) + int(s[i]))
        
        return s if not res else res+s[-1] if s[-1].isalpha() else res