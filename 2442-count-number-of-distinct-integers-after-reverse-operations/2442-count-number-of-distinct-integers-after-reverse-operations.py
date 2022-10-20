class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
            rev = 0
            while num > 0:
                rev = (rev * 10) + (num % 10)
                num //= 10
            s.add(rev)
        return len(s)