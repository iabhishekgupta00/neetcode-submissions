
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        for n in nums:
            newdp = {}

            for total, count in dp.items():
                newdp[total + n] = newdp.get(total + n, 0) + count
                newdp[total - n] = newdp.get(total - n, 0) + count

            dp = newdp

        return dp.get(target, 0)
     
