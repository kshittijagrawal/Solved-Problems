class Solution:
    def minTimeToType(self, word: str) -> int:
        curr, finalgap = ord("a") - 96, 0
        for c in word:
            currgap = ord(c) - 96 - curr if ord(c) - 96 - curr >= 0 else curr - (ord(c) - 96)
            finalgap += min(currgap, 26 - currgap)
            curr = ord(c) - 96
            
        return finalgap + len(word)