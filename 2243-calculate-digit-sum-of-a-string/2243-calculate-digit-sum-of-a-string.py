class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            arr, c, sum = [], k, 0
            for i in range(len(s)):
                if c == 0:
                    arr.append(str(sum))
                    sum, c = 0, k
                sum += int(s[i])
                c -= 1
            arr.append(str(sum))
            s = "".join(arr)
        
        return s