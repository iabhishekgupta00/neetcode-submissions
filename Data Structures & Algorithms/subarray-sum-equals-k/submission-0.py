class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {0: 1}
        total = 0
        res = 0

        for n in nums:
            total += n

            diff = total - k

            if diff in count:
                res += count[diff]

            count[total] = count.get(total, 0) + 1

        return res