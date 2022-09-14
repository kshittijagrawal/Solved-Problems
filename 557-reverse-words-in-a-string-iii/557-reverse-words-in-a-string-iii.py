class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in map(list, s.split()):
            lo, hi = 0, len(word) - 1
            while lo < hi:
                word[lo], word[hi] = word[hi], word[lo]
                lo += 1
                hi -= 1
            res.append("".join(word))
        return " ".join(res)
                