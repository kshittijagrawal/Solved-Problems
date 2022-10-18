class Solution:
    def countAndSay(self, n: int) -> str:
        
        def isSaid(num, curr):
            if curr == n:
                return num
            currcount, currdigit = 1, num[0]
            res = []
            
            for i in range(1, len(num)):
                if num[i] == currdigit:
                    currcount += 1
                else:
                    res.append(str(currcount))
                    res.append(currdigit)
                    currcount, currdigit = 1, num[i]
            res.append(str(currcount))
            res.append(currdigit)
            
            return isSaid("".join(res), curr + 1)
        
        return isSaid("1", 1)
        
        
                