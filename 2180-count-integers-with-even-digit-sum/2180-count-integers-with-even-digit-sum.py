class Solution:
    def countEven(self, num: int) -> int:
        # res = 0
        # for i in range(1, num + 1):
        #     sum = 0
        #     while i > 0:
        #         sum += i % 10
        #         i //= 10
        #     if sum % 2 == 0:
        #         res += 1
        # return res
        
        temp, sum = num, 0
        while temp > 0:
            sum += temp % 10
            temp //= 10
        return num // 2 if sum % 2 == 0 else (num - 1) // 2