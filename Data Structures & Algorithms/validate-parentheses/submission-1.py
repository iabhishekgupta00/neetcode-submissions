class Solution:
    def isValid(self, s):
        stack = []
        p = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != p[ch]:
                    return False
                stack.pop()

        return not stack