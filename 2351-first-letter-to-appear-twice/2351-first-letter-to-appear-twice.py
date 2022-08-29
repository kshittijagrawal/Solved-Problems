class Solution:
    def repeatedCharacter(self, s: str) -> str:
        container = set()
        for c in s:
            if c in container:
                return c
            container.add(c)
        return -1