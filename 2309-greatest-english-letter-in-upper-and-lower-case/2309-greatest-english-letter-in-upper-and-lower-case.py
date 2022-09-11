class Solution:
    def greatestLetter(self, s: str) -> str:
        container = set()
        cand = ""
        for c in s:
            if chr(ord(c) - 32) in container or chr(ord(c) + 32) in container:
                if not cand: cand = c.upper()
                else:
                    cand = cand if cand > c.upper() else c.upper()
            container.add(c)
        return cand