import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        minHeap = [(0, k)]
        dist = {}

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in dist:
                continue

            dist[node] = time

            for nei, w in graph[node]:
                if nei not in dist:
                    heapq.heappush(minHeap, (time + w, nei))

        if len(dist) == n:
            return max(dist.values())

        return -1