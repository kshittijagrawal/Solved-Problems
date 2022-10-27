class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
	    container = {0: -1}
	    curr = 0
        
	    for i, num in enumerate(nums):
		    curr = (curr + num) % k
		    if curr in container:
			    if i - container[curr] >= 2:
				    return True
		    else:
			    container[curr] = i
	    return False