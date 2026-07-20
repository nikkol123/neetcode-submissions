class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMax = 0
        buy = float("inf")
        for price in prices:
            profit = price - buy
            if profit > localMax: localMax = profit
            if price < buy: buy = price
        return localMax