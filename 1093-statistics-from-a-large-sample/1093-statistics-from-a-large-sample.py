class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        
        mn, mx, mode, max_freq, sm, total = float('+inf'), float('-inf'), 0, 0, 0, 0
        arr = []
        
        for i, el in enumerate(count):
            if el > 0: 
                mn = min(mn, i)
                mx = max(mx, i)
            if el > max_freq:
                mode = i
                max_freq = el
                
            sm += el * i
            total += el
            arr.append(total)
            
        median1 = bisect.bisect(arr, (total - 1) // 2)
        median2 = bisect.bisect(arr, total // 2)
        return [mn, mx, sm / total, (median1 + median2) / 2, mode]