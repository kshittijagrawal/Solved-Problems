class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        if(not nums):
            return []
        result = []
        
		#helper method
        def isArithmetic(split):
            split.sort()
            d = abs(split[1]-split[0])
            for i in range(2,len(split)):
                if(abs(split[i]-split[i-1])==d):
                    continue
                else:
                    return False
            return True
                
        for a,b in zip(l,r):
			#edge case check
            if(abs(a-b)+1<2):
                result.append(False)
            else:
                split = nums[a:b+1]
                if(isArithmetic(split)):
                    result.append(True)
                else:
                    result.append(False)
        return result