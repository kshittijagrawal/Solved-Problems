class Solution:
    def frequencySort(self, s: str) -> str:
        freqs = collections.Counter(s)
        arr = [""] * (len(s) + 1)
        
        for k, v in freqs.items():
            arr[v] += k * v
            
        res = []
        for i in range(len(s), -1, -1):
            res.append(arr[i])
        
        return "".join(res)