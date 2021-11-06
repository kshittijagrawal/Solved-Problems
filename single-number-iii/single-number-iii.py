class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        f =  None
        for i in range(len(nums)):
            if c[nums[i]] == 1:
                if f is None:
                    f = nums[i]
                else:
                    return [f, nums[i]]