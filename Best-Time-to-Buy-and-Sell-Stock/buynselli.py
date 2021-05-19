class Solution:
    def maxProfit(self, prices):
        _min, sub, res = prices[0], 0, 0
        for i in range(0, len(prices)):
            _min = min(_min, prices[i])
            if (prices[i] - _min) > 0:
                sub = prices[i] - _min
            if sub > res:
                res = sub
        return res
        