class Solution:
    def minCostClimbingStairs(self, cost):
        one = 0
        two = 0

        for i in range(2, len(cost) + 1):
            one, two = two, min(
                two + cost[i - 1],
                one + cost[i - 2]
            )

        return two