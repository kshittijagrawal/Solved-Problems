class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        curr_count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "-":
                continue
            if curr_count == k:
                res = "-" + res
                curr_count = 0
            res = s[i].upper() + res
            curr_count += 1
        return res