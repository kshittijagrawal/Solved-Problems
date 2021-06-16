class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n+1)]
        i = 0
        while n != 1:
            i = (i+(k-1))%n
            del nums[i]
            n -= 1
        return nums[0]