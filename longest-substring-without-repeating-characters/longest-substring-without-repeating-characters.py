class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        beg, end, S, curr, res = 0, 0, set(), 0, 0
        while end < len(s):
            if s[end] not in S:
                curr += 1
                S.add(s[end])
                end += 1
                res = max(res, curr)
            else:
                S.remove(s[beg])
                curr -= 1
                beg += 1
        return res