class Solution:
    def lengthOfLastWord(self, s):
        flag, count = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and flag == 0:
                continue
            elif s[i] == " " and flag == 1:
                return count
            else:
                flag = 1
                count += 1
        return count