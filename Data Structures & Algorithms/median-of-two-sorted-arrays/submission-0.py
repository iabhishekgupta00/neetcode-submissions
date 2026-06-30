from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m

        while True:
            i = (l + r) // 2          # partition nums1
            j = half - i              # partition nums2

            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')

            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Correct partition
            if left1 <= right2 and left2 <= right1:

                if total % 2:  # odd length
                    return min(right1, right2)
                else:          # even length
                    return (max(left1, left2) + min(right1, right2)) / 2

            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1