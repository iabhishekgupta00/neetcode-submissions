class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = {}
        for i , num in enumerate(numbers):
            b = target - num
            if b in a:
                return [a[b] + 1,i + 1]
            a[num] = i


        