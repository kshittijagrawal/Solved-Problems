class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        container = set()
        res = 0
        for num in nums:
            if num * -1 in container and abs(num) > res:
                res = abs(num)
            container.add(num)
        return res if res else -1