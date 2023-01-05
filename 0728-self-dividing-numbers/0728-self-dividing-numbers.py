class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def check(num):
            dupnum = num
            while num > 0:
                d = num % 10
                if (d == 0) or (dupnum % d != 0):
                    return 0
                num //= 10
            return 1
        
        res = []
        for i in range(left, right + 1):
            if check(i):
                res.append(i)
        return res