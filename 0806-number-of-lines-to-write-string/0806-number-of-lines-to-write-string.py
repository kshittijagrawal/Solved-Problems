class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = prev = 0
        for c in s:
            prev += widths[ord(c) - 97]
            if prev > 100:
                line, prev = line + 1, widths[ord(c) - 97]
        return [line + 1, prev]