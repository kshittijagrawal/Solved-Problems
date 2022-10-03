class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = {}
        for num in nums:
            if c.get(num):
                c[num] -= 1
            else:
                c[num] = 1
            if not c.get(num):
                del c[num]
        return not(bool(c))