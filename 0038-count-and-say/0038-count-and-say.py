class Solution:
    def countAndSay(self, n: int) -> str:
        
        def isSaid(num):
            currcount, currnum = 0, num % 10
            pattern = []
            while num > 0:
                if num % 10 == currnum:
                    currcount += 1
                else:
                    pattern.append([currcount, currnum])
                    currcount, currnum = 1, num % 10
                num //= 10
            pattern.append([currcount, currnum])
            
            res = []
            for i in range(len(pattern) - 1, -1, -1):
                res.append(pattern[i][0])
                res.append(pattern[i][1])
            
            return "".join(list(map(str, res)))
        
        cas = ""
        for i in range(1, n + 1):
            if i == 1:
                cas = "1"
            else:
                cas = isSaid(int(cas))
        return cas
                