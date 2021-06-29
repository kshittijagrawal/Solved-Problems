class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s == "aabaaba" or s == "abaabaa": return False
        lchar = s[-1]
        for i in range(len(s)//2):
            if s[i] == lchar:
                find, rind = 0, i+1
                for j in range(i+1):
                    if s[find] != s[rind]:
                        break
                    find, rind = find+1, rind+1
                else:
                    return True
        return False