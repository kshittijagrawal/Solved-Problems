class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = curr = 1
        for i in range(1, len(s)):
            if s[i] == chr(ord(s[i - 1]) + 1):
                curr += 1
            else:
                res, curr = max(curr, res), 1
        return max(res, curr)