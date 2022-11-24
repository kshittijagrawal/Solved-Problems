class Solution:
    def largestInteger(self, num: int) -> int:
        odds, evens = [], []
        n, r, num_count = num, 0, 0
        
        while n > 0:
            d = n % 10
            if d % 2 == 0:
                evens.append(n % 10)
            else:
                odds.append(n % 10)
            r = r * 10 + d
            num_count += 1
            n //= 10
        
        odds.sort()
        evens.sort()
        
        res = rev_count = 0
        while r > 0:
            d = r % 10
            if d % 2 == 0:
                res = res * 10 + (evens.pop())
            else:
                res = res * 10 + (odds.pop())
            rev_count += 1
            r //= 10
        
        for _ in range(num_count - rev_count):
            res = res * 10 + (evens.pop())
        return res
