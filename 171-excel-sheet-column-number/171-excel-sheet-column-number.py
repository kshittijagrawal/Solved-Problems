class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res, n = 0, len(columnTitle)
        for c in columnTitle:
            res += (26**(n-1)) * (ord(c) - 64)
            n -= 1
        return res