class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] - (mid + 1) < k:
                lo = mid + 1
            else:
                hi = mid
        
        if lo == len(nums) - 1 and nums[lo] - lo - 1 < k:
            return lo + k + 1
        return lo + k
                