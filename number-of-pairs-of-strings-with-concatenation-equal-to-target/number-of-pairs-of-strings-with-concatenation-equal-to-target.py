class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        container, res = {}, 0
        tlen = len(target)
        for i in range(len(nums)):
            ilen = len(nums[i])
            if target[:ilen] == nums[i] and target[ilen:] in container:
                res += container[target[ilen:]]
            if target[tlen - ilen:] == nums[i] and target[:tlen - ilen] in container:
                res += container[target[:tlen - ilen]]
            container[nums[i]] = container.get(nums[i], 0) + 1
        
        return res