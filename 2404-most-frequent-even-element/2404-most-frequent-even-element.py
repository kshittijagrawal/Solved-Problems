class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        container, res = {-1: -1}, -1
        for num in nums:
            if num % 2 != 0: continue
            container[num] = container.get(num, 0) + 1
            
            if container[num] > container[res]:
                res = num
            elif container[num] == container[res]:
                res = res if res < num else num
        return res
                