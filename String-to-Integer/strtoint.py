class Solution:
    def myAtoi(self, s):
        num = ""
        for ch in s:
            if ch == " " and len(num)==0:
                continue
            if ch in "+-":
                if not num:
                    num += ch
                    continue
                elif num[-1] not in "0123456789":
                    return 0
                else:
                    break
            if ch.isdigit():
                num += ch
            else:
                break
        if not num or (len(num) == 1 and num[0] in "+-"):
            return 0
        positivity = -1 if num[0] is "-" else 1
        num = positivity*int(num.strip("+-"))
        if num > 2**31 - 1:
            return 2**31 - 1
        elif num < -2**31:
            return -2**31
        return num