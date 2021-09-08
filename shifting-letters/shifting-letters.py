class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res, postsum = [""] * len(s), 0
        for i in range(len(s) - 1, -1, -1):
            postsum += shifts[i]
            res[i] = chr(((ord(s[i]) - 97 + postsum) % 26) + 97)
            
        return "".join(res)