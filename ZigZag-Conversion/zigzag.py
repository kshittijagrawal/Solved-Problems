class Solution:
    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s
        res = [""] * numRows
        i, flag = 0, 1
        for el in s:
            if i == 0 and flag == 1:
                res[i] += el
                i += 1
            elif i == 0 and flag == 0:
                i += 1
                res[i] += el
                flag, i = 1, i+1
            elif i < numRows and flag == 1:
                res[i] += el
                i += 1
            elif i < numRows and flag == 0:
                i -= 1
                res[i] += el
            else:
                flag, i = 0, i-2
                res[i] += el
        return "".join(res)