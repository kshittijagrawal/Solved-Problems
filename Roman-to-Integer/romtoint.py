class Solution:
    def romanToInt(self, s):
        d = {"I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000}
        total, curr = 0, 0
        for i, el in enumerate(s):
            if d[el] <= curr or i == 0:
                total += d[el]
                curr = d[el]
            else:
                total = total + d[el] - 2*d[s[i-1]]
                
        return total