class Solution:
    def maxArea(self, h) :
        l = 0
        r = len(h) - 1
        max_water = 0

        while l < r:
            width = r - l
            curr_water = min(h[l], h[r]) * width
            max_water = max(max_water, curr_water)

            if h[l] < h[r]:
                l += 1
            else:
                r -= 1

        return max_water