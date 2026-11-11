class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = [-i for i in nums]
        heapq.heapify(self.nums)
        self.k = k
        print(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        popped = []
        for _ in range(self.k):
            ans = heapq.heappop(self.nums)
            popped.append(ans)
        for num in popped:
            heapq.heappush(self.nums, num)
        return -ans
        
