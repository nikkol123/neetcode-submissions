from collections import Counter
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        queue = deque() # [-count, nextTimeAvailable]
        time = 0

        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append([cnt, time + n])

            if queue and time >= queue[0][1]:
                cnt, _ = queue.popleft()
                heapq.heappush(maxHeap, cnt)  

        return time



        