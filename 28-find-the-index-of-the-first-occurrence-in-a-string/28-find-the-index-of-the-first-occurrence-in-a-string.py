class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        for i in range(0, n - m + 1):
            iprime, j = i, 0
            while haystack[iprime] == needle[j]:
                if j == m-1: break
                iprime += 1
                j += 1
            else: continue
            return i
        return  -1