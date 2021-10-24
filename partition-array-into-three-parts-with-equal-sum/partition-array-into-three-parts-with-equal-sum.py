class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        tsum = sum(arr)
        if tsum % 3 != 0: return False
        each, count, curr = tsum // 3, 0, 0
        
        for i in range(len(arr)):
            curr += arr[i]
            if curr == each:
                count += 1
                curr = 0
            if count == 2 and i < len(arr)-1:
                break
        else:
            return False
        return True
        
        