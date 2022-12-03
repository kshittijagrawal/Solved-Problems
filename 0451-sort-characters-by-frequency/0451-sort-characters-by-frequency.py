class Solution:
    def frequencySort(self, s: str) -> str:
        c, size = {}, 0
        for ch in s:
            c[ch] = c.get(ch, 0) + 1
            size = max(size, c[ch])
        
        arr = [""] * (size + 1)
        
        for k in c:
            arr[c[k]] += k * c[k]
        
        return "".join(arr[::-1])