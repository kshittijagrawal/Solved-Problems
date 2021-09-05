class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ei, oi = 0, 1
        while ei < len(nums) and oi < len(nums):
            if nums[ei] % 2 != 0 and nums[oi] % 2 == 0:
                nums[ei], nums[oi] = nums[oi], nums[ei]
                ei += 2
                oi += 2
            elif nums[ei] % 2 == 0 and nums[oi] % 2 != 0:
                ei += 2
                oi += 2
            elif nums[ei] % 2 == 0 and nums[oi] % 2 == 0:
                ei += 2
            else:
                oi += 2
        
        return nums