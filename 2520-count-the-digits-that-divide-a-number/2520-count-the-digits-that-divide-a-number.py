class Solution:
    def countDigits(self, num: int) -> int:
        res, dupnum = 0, num
        while num > 0:
            if dupnum % (num % 10) == 0:
                res += 1
            num //= 10
        return res