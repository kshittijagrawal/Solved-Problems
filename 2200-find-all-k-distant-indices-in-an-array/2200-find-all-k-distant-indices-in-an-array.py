class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            if num == key:
                start = max(i - k, 0)
                end = min(i + k, len(nums) - 1)
                
                if res and start <= res[-1]:
                    start = res[-1] + 1
                
                for j in range(start, end + 1):
                    res.append(j)
        return res