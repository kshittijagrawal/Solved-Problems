class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        try: a = arr[1]
        except: return 1
        
        s, res, t, e = 0, 0, 0, 1
        
        for e in range(1, len(arr)):
            if arr[e-1] > arr[e]:
                if t == 1:
                    res = max(res, e - s)
                    s = e - 1
                t = 1
            
            elif arr[e-1] < arr[e]:
                if t == -1:
                    res = max(res, e - s)
                    s = e - 1
                t = -1
            
            else:
                res = max(res, e - s)
                s = e
                t = 0
        
        return max(res, e - s + 1)