class Solution:
    def frequencySort(self, s: str) -> str:
        container = collections.Counter(s)
        freqs = {k:v for k,v in sorted(container.items(), key = lambda x: x[1], reverse = True)}
        res = ""
        
        for key, val in freqs.items():
            res += (key*val)
            
        return res