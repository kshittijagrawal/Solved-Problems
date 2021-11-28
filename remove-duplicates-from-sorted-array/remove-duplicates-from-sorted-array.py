class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        currmax, j = nums[0], 1
        for i in range(1, len(nums)):
            if nums[i] > currmax:
                currmax = nums[i]
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return j