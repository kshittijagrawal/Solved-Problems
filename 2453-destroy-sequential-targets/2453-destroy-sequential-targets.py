class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        container = {}
        currmax = float("-inf")
        for num in nums:
            container[num % space] = container.get(num % space, 0) + 1
            currmax = max(currmax, container[num % space])
        
        # print(container, currmax)
        res = float("inf")
        for num in nums:
            if container[num % space] == currmax:
                res = min(res, num)
        return res