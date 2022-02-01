class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr, res = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < curr: curr = prices[i]
            if prices[i] - curr > res: res = prices[i] - curr
        return res