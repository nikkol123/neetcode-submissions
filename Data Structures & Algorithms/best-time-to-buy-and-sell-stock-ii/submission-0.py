class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit=0
        if not prices: return 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > 0:
                profit += prices[i] - buy
                buy = prices[i]
        return profit

            


        