class StockSpanner:

    def __init__(self):
        self.stack = [] #price span

    def next(self, price: int) -> int:
        # return the span for today stock's prices
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            val, prev_span = self.stack.pop()
            span += prev_span
        self.stack.append([price, span])
        return self.stack[-1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)