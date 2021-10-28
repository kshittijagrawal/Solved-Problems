class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        k = 0 # can be used for any other number as well
        s = set()
        
        for i in range(n - 2):
            container = {}
            
            for j in range(i+1, n):
                c = k - nums[i] - nums[j]
                if c in container and (nums[i], nums[j], c) not in s:
                    res.append([nums[i], nums[j], c])
                    s.add((nums[i], nums[j], c))
                    s.add((nums[i], c, nums[j]))
                    s.add((nums[j], nums[i], c))
                    s.add((nums[j], c, nums[i]))
                    s.add((c, nums[i], nums[j]))
                    s.add((c, nums[j], nums[i]))
                    container[c] -= 1
                    if container[c] <= 0:
                        del container[c]
                container[nums[j]] = container.get(nums[j], 0) + 1
        
        return res
                    