class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s_num = set(nums)
        long = 0

        for n in s_num:
            if n - 1 not in s_num:
                curr = n
                length = 1

                while curr + 1 in s_num:
                    curr += 1
                    length += 1

                long = max(long,length)

        return long
        
        