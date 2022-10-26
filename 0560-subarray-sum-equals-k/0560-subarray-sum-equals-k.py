class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        container = {0: 1}
        presum = res = 0
        
        for num in nums:
            presum += num
            tocheck = presum-k
            if container.get(tocheck, 0):
                res += container.get(tocheck)
            container[presum] = container.get(presum, 0) + 1
        return res