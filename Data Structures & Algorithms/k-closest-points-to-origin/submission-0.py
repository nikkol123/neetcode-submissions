import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        entries = []

        for point in points:
            x, y = point
            entries.append((-(x**2 + y**2), point))

        print(entries)
       
        heapq.heapify(entries)
        while len(entries)>k:
            heapq.heappop(entries)
        
        print(entries)
        
        out = []
        for dist, point in entries:
            out.append(point)
        return out
