class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_l = [0] * n
        max_r = [0] * n

        for i in range(n):
            j = -i - 1
            max_l[i] = l_wall
            max_r[j] = r_wall
            l_wall = max(l_wall , height[i])
            r_wall = max(r_wall , height[j])

        sum = 0
        for i in range(n):
            pot = min(max_l[i] , max_r[i])
            sum += max(0 , pot - height[i] )
        return sum