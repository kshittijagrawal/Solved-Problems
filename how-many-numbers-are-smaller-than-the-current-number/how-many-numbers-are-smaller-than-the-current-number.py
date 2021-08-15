class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = [0]*101
        for num in nums:
            freq[num] += 1
        
        s, curr = 0, 0
        for i in range(101):
            curr = freq[i]
            s += curr
            if not curr: continue
            freq[i] = s - curr
        
        return [freq[num] for num in nums]