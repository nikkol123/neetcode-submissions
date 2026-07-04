from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        #B+ student note. Don't forget to append "x"
        self.queue.append(x)

    def pop(self) -> int:
        temp1 = self.queue.pop()
        for i in range(len(self.queue)):
            temp2 = self.queue.pop()
            self.queue.append(temp2)
        return temp1



    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()