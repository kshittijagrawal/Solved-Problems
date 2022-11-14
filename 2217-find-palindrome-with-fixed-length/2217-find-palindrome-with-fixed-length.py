class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        rootLength = (intLength + 1) // 2
        maxPossible = 10 ** (rootLength - 1) * 9
        
        root = str(10 ** (intLength - 1))[:rootLength]
        
        res = []
        for q in queries:
            if q > maxPossible:
                res.append(-1)
            else:
                pre = str(int(root) + (q - 1))
                if intLength % 2 == 0:
                    res.append(int(pre + pre[::-1]))
                else:
                    res.append(int(pre + pre[::-1][1:]))
        return res
            
        