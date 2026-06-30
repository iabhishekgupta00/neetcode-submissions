from math import ceil,floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in '+-/*':
                b,a = stack.pop() , stack.pop()

                if t == '+':
                    stack.append(a+b)

                elif t == '-':
                    stack.append(a-b)

                elif t == '*':
                    stack.append(a*b)

                else:
                    division = a/b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(floor(division))

            else:
                stack.append(int(t))


        return stack[0]
        