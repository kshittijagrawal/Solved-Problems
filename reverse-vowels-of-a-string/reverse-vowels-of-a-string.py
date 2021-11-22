class Solution:
    def reverseVowels(self, s: str) -> str:
        s, lo, hi, vowels = list(s), 0, len(s) - 1, {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while lo < hi:
            while lo < hi and s[lo] not in vowels: lo += 1
            while lo < hi and s[hi] not in vowels: hi -= 1
            s[lo], s[hi] = s[hi], s[lo]
            lo, hi = lo + 1, hi - 1
        return "".join(s)