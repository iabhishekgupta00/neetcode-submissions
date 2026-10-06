import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        queries = sorted((q, i) for i, q in enumerate(queries))

        heap = []
        ans = [-1] * len(queries)

        i = 0

        for q, index in queries:

            # Add intervals that can contain q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1

            # Remove intervals that ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Smallest valid interval
            if heap:
                ans[index] = heap[0][0]

        return ans