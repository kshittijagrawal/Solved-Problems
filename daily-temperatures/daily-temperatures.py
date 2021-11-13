class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res, stack = [0] * len(temps), collections.deque()
        for i in range(len(temps)):
            while stack and temps[i] > temps[stack[-1]]:
                pre = stack.pop()
                res[pre] = i - pre
            stack.append(i)
        return res