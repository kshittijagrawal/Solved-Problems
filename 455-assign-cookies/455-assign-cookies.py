class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res, gi, si = 0, 0, 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                res += 1
                gi, si = gi + 1, si + 1
            else:
                si += 1
        return res