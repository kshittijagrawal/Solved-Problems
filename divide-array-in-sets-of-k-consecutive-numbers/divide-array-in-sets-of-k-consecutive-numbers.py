class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k != 0: return False
        
        nums = sorted(nums)
        container, index = collections.Counter(nums), 0
        
        while index < n:
            curr = nums[index]
            for i in range(k):
                if not container.get(curr+i, 0):
                    return False
                container[curr+i] -= 1
                if container[curr+i] == 0:
                    del container[curr+i]
                  
            index += 1
            while index < n and (not container.get(nums[index], 0)):
                index += 1
        
        return True
            