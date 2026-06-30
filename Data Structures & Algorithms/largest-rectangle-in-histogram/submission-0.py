class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        max_area = 0

        for i , heights in enumerate(heights):
            start = i
            while stack and heights < stack[-1][0]:
                h , j = stack.pop()
                w = i - j
                a = h*w
                max_area = max(max_area , a)
                start = j
            stack.append((heights , start))

        while stack:
            h , j = stack.pop()
            w = n - j
            max_area = max(max_area , h*w)

        return max_area