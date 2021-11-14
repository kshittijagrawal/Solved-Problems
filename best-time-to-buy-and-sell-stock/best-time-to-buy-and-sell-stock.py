class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, curr = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] < curr:
                curr = prices[i]
                continue
            res = max(res, prices[i] - curr)
        return res