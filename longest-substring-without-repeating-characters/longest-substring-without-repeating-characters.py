class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        container, start, end, res, curr = set(), 0, 0, 0, 0
        while end < len(s):
            if s[end] not in container:
                container.add(s[end])
                end += 1
                curr += 1
            else:
                res = max(res, curr)
                container.remove(s[start])
                start += 1
                curr -= 1
        
        return max(res, curr)