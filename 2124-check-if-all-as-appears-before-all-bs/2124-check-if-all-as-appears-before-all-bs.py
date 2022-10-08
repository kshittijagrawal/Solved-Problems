class Solution:
    def checkString(self, s: str) -> bool:
        res = True
        for i in range(1, len(s)):
            if ord(s[i - 1]) > ord(s[i]):
                res = False
                break
        return res