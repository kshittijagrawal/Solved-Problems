class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split(" ")
        maxlen = len(max(arr, key = len))
        
        res = [""] * maxlen
        for i in range(maxlen):
            for j in range(len(arr)):
                try: res[i] += arr[j][i]
                except: res[i] += " "
        
        for i in range(maxlen):
            if res[i][-1] == " ":
                res[i] = res[i].rstrip()
        
        return res