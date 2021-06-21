class Solution:
    def largestOddNumber(self, num: str) -> str:
        n, ind = len(num), -1
        for i in range(n-1, -1, -1):
            if int(num[i])%2 != 0:
                ind = i
                break
        
        return num[:ind+1] if ind != -1 else ""