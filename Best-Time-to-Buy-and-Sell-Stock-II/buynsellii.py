class Solution:
    def maxProfit(self, prices):
        res = 0
        for i in range(0, len(prices)-1):
            if prices[i] < prices[i+1]:
                res += prices[i+1]-prices[i]
        return res