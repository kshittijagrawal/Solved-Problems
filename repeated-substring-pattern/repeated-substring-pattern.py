class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lchar, length = s[-1], len(s)
        for i in range(length//2):
            if s[i] == lchar:
                if s[:i+1]*(length//(i+1)) == s:
                    return True
        return False
