class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        res = 0

        for n in nums:
            if res < 0:
                res = 0
            res += n
            maxSub = max(maxSub , res)
        return maxSub

