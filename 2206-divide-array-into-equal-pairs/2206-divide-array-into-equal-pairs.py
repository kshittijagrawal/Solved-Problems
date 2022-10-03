class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for k in c:
            if c[k] % 2:
                return False
        return True