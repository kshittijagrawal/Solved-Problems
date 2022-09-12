class Solution:
    def partitionString(self, s: str) -> int:
        container, res = set(), 1
        for c in s:
            if c in container:
                res += 1
                container.clear()
            container.add(c)
        return res