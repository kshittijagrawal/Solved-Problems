class Solution:
    def longestPalindrome(self, s: str) -> int:
        res, oddcounted = 0, 0
        container = collections.Counter(s)
        for char, freq in container.items():
            if freq % 2 != 0:
                if oddcounted == 0:
                    res += freq
                    oddcounted = 1
                else:
                    res += (freq-1)
            else:
                res += freq
        return res
                
        
        