class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1]*(k+1)
        self.head, self.tail = 0, 0
        self.n = len(self.queue)

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.n
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = -1
            self.head = (self.head + 1) % self.n
            return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[self.tail-1]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail + 1) % self.n == self.head


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()