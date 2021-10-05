class Solution:
    def climbStairs(self, n: int, mem={1:1,2:2,3:3}) -> int:
        if n in mem:
            return mem[n]
        mem[n] = self.climbStairs(n-1, mem) + self.climbStairs(n-2, mem)
        return mem[n]