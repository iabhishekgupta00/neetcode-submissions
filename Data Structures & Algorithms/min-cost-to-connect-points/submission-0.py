import heapq
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        minHeap = [(0, 0)]
        visit = set()
        res = 0

        while len(visit) < n:
            cost, i = heapq.heappop(minHeap)

            if i in visit:
                continue

            visit.add(i)
            res += cost

            x1, y1 = points[i]

            for j in range(n):
                if j not in visit:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minHeap, (dist, j))

        return res