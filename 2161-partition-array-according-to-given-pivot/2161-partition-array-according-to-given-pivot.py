class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        ans = [pivot] * n
        left, right = 0, -1
        
        for i, num in enumerate(nums):
            if num < pivot:
                ans[left], left = num, left + 1
            if nums[~i] > pivot:
                ans[right], right = nums[~i], right - 1
                
        return ans   