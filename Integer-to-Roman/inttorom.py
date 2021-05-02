class Solution:
    def intToRoman(self, num):
        d = {1000:"M",
             900:"CM",
             500:"D",
             400:"CD",
             100:"C",
             90:"XC",
             50:"L",
             40:"XL",
             10:"X",
             9:"IX",
             5:"V",
             4:"IV",
             1:"I"}
        s = ""
        for i in d.keys():
            if num//i == 0:
                continue
            s = s + (d[i] * (num//i))
            num %= i
        return s
            