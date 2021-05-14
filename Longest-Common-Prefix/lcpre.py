class Solution:
    def longestCommonPrefix(self, strs):
        res = ""
        check = sorted(strs, key = lambda x: len(x))
        check = check[0]
        for i in range(len(check)):
            flag = 0
            for j in strs:
                if j[i] != check[i]:
                    flag = 1
                    break
            if flag == 0:
                res += check[i]
            else:
                return res
        return res
        