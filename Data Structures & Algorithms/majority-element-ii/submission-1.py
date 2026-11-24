from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num1 = num2 = None
        count1 = count2 = 0

        # Find two possible candidates
        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1
            elif count1 == 0:
                num1 = n
                count1 = 1
            elif count2 == 0:
                num2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Verify candidates
        res = []
        count1 = count2 = 0

        for n in nums:
            if n == num1:
                count1 += 1
            elif n == num2:
                count2 += 1

        if count1 > len(nums) // 3:
            res.append(num1)

        if count2 > len(nums) // 3:
            res.append(num2)

        return res