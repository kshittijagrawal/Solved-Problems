class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = collections.Counter(s)
        res, oddfound = 0, 0
        for k in c:
            if c[k] % 2 == 0:
                res += c[k]
            else:
                if not oddfound:
                    oddfound = 1
                    res += 1
                res += c[k] - 1
                
        return res