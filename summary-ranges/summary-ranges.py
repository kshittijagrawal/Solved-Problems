class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        res, upper, lower = [], nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i-1]+1 == nums[i]:
                upper = nums[i]
            else:
                res.append(f"{lower}->{upper}" if lower != upper else f"{lower}")
                lower, upper = nums[i], nums[i]
        res.append(f"{lower}->{upper}" if lower != upper else f"{lower}")
        return res