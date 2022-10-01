class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for word in words:
            if s[:len(word)] == word: res += 1
        return res