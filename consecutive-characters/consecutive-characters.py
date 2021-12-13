class Solution:
    def maxPower(self, s: str) -> int:
        curr, res = 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        return max(res, curr)