class Solution:
    def searchRange(self, nums, target):
        lo, hi, pble = 0, len(nums)-1, -1
        while lo<=hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] == target:
                pble = mid
                break
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        if pble < 0: return [-1,-1]
        
        lo, hi, end = pble, len(nums)-1, 0
        while lo<=hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] == target:
                end = mid
                lo = mid+1
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
                
        lo, hi, start = 0, pble, pble
        while lo<=hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] == target:
                start = mid
                hi = mid-1
            elif nums[mid] < target:
                lo = mid+1
            else:
                hi = mid-1
                
        return [start, end]