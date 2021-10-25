class Solution:
    def thousandSeparator(self, n: int) -> str:
        res, s, c = collections.deque(), str(n), 0
        for i in range(len(s) - 1, -1, -1):
            if c == 3:
                c = 0
                res.appendleft(".")
            res.appendleft(s[i])
            c += 1
        return "".join(res)