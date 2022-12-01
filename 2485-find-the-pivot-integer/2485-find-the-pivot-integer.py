class Solution:
    def pivotInteger(self, n: int) -> int:
        
        def sum_till_n(num):
            return num * (num + 1) // 2
        
        res = None
        for i in range(n // 2, n + 1):
            till_i = sum_till_n(i)
            
            # print(i, till_i, sum_till_n(n) - till_i + i)
            if till_i == sum_till_n(n) - till_i + i:
                res = i
                break
        
        return res if res else -1