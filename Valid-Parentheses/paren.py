class Solution:
    def isValid(self, s):
        if len(s)%2 != 0:
            return False
        while s != "":
            if s.find("[]") != -1:
                s = s[:s.index("[]")] + s[s.index("[]")+2:]
            elif s.find("()") != -1:
                s = s[:s.index("()")] + s[s.index("()")+2:]
            elif s.find("{}") != -1:
                s = s[:s.index("{}")] + s[s.index("{}")+2:]
            else:
                return False
        return True