class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # minPrice = float("inf")
        # for price in prices:
        #     profit = price - minPrice
        #     res = max(profit, res)
        #     minPrice = min(minPrice, price)
        # return res

        left, right = 0, 1
        maxProfit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right+=1
        return maxProfit





