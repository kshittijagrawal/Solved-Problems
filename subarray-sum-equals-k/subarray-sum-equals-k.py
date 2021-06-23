class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        repo, count, presum = {}, 0, 0
        repo[0] = 1
        
        for num in nums:
            presum += num
            if presum-k in repo:
                count += repo[presum-k]
            repo[presum] = repo.get(presum, 0) + 1
        return count