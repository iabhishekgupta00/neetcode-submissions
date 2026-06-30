class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = len(temperatures)
        res = [0] * temp
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackTemp , stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res
        