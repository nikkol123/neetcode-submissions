class MinStack:

    def __init__(self):
        self.stack = []
        self.miniStack = [float('inf')]

    def push(self, val: int) -> None:
        if val <= self.miniStack[-1]: self.miniStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.miniStack[-1]:
            self.miniStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.miniStack[-1]
