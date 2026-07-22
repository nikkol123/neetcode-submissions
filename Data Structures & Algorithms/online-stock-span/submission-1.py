class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        # return the span for today stock's prices
        count = 1
        if self.stack: 
            for i in range(len(self.stack)-1, -1, -1):
                if price >= self.stack[i]: count+=1
                else: break
        self.stack.append(price)
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)