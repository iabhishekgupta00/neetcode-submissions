class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in char:
                if stack and stack[-1] == char[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return len(stack) == 0
        