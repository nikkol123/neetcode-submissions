class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minPrice = float("inf")
        for price in prices:
            profit = price - minPrice
            res = max(profit, res)
            minPrice = min(minPrice, price)
        return res
