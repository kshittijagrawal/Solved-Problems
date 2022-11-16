class Solution:
    def countAsterisks(self, s: str) -> int:
        onoff = res = 0
        for c in s:
            if onoff and c != "|":
                continue
            if c == "*":
                res += 1
            if c == "|":
                onoff = not onoff
        return res