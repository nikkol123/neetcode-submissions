class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        entries = []

        for point in points:
            x, y = point
            entries.append((x**2 + y**2, point))
       
        heapq.heapify(entries)
        out = []
        for _ in range(k):
            out.append(heapq.heappop(entries))
        print(out)

        return [point for dist, point in out]
