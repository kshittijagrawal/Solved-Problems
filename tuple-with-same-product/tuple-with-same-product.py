class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = {}
        count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                curr = nums[i]*nums[j]
                count += (prods.get(curr, 0))
                prods[curr] = prods.get(curr, 0) + 1
                
        return count*8