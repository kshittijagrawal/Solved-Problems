class Solution: 
	def smallestValue(self, n: int) -> int: 
        
		while True: 
			nn, sm = n, 0
			for f in range(2, nn+1): 
				while nn % f == 0: 
					nn //= f 
					sm += f
			if sm == n: break 
			n = sm
            
		return n