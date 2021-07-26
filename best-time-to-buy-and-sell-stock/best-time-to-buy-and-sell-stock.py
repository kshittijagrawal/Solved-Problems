class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmin, res = prices[0], 0
        for price in prices[1:]:
            if price < currmin: currmin = price
            if price - currmin > res: res = price - currmin
        return res