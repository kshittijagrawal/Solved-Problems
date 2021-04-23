import re
class Solution:
    def isMatch(self, s, p):
        special = ".*"
        if special[0] not in p and special[1] not in p:
            return s==p
        res = re.fullmatch(p, s)
        if res is not None:
            return True
        return False