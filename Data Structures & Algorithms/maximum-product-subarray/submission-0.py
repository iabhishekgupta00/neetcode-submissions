class Solution:
    def maxProduct(self, nums):
        curMax = curMin = nums[0]
        ans = nums[0]

        for n in nums[1:]:
            if n < 0:
                curMax, curMin = curMin, curMax

            curMax = max(n, curMax * n)
            curMin = min(n, curMin * n)

            ans = max(ans, curMax)

        return ans