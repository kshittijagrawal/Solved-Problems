class Solution:
    def maximumNumber(self, nums: str, change: List[int]) -> str:
        num , flag = list(nums), 0
        for i in range(len(num)):
            curr = int(num[i])
            if change[curr] > curr:
                num[i] = str(change[curr])
                flag = 1
            elif change[curr] < curr and flag:
                break
        
        return "".join(num)