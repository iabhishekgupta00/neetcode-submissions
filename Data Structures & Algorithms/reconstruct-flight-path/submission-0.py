from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []

        def dfs(src):
            while graph[src]:
                nei = graph[src].pop()
                dfs(nei)

            res.append(src)

        dfs("JFK")

        return res[::-1]