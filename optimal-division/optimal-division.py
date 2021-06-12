class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        else:
            return "{}/({})".format(nums[0], "/".join(list(map(str, nums[1:]))))