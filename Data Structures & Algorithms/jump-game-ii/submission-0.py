class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r =0
        
        while r < len(nums) - 1:
            fath = 0
            for i in range(l,r + 1):
                fath = max(fath,i + nums[i])
            l = r + 1
            r = fath
            res += 1
        return res
