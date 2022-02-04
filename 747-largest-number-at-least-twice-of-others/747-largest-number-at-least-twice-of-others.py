class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        fmax = smax = ind = -1
        for i in range(len(nums)):
            if nums[i] > fmax:
                smax = fmax
                fmax = nums[i]
                ind = i
            elif nums[i] > smax and nums[i] != fmax:
                smax = nums[i]
        
        if fmax >= smax * 2:
            return ind
        if smax == -1:
            return 0
        return -1