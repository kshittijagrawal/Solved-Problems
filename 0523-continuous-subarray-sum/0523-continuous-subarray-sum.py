class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
	    remainders = {0: -1}
	    curr_rem = 0
        
	    for i, num in enumerate(nums):
		    curr_rem = (curr_rem + num) % k
		    if curr_rem in remainders:
			    if remainders[curr_rem] < i-1:
				    return True
		    else:
			    remainders[curr_rem] = i
	    return False