#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start

import math


class Solution:

    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])

        def calculation(a: str, b: str, operator: str) -> int:
            if operator == "+":
                return int(a) + int(b)
            elif operator == "-":
                return int(a) - int(b)
            elif operator == "*":
                return int(a)*int(b)
            else:
                tmp = int(a)/int(b)
                # leaning towards 0
                return math.floor(tmp) if tmp > 0 else math.ceil(tmp)

        stack = []
        operator = ["+", "-", "*", "/"]

        for char in tokens:
            if char in operator:
                a = stack.pop()
                b = stack.pop()
                ans = calculation(b, a, char)
                stack.append(ans)
            else:
                stack.append(char)

        return stack[0]

        #     if ans == 0 and len(stack) >= 2:
        #         a = stack.pop()
        #         b = stack.pop()
        #         ans = calculation(b, a,  char)
        #         print(ans)
        #     else:
        #         a = stack.pop()
        #         if len(stack) == 0:
        #             ans = calculation(ans, a, char)
        #         else:
        #             ans = calculation(a, ans, char)
        #         print(ans)
        # else:
        #     stack.append(char)

        return ans

        # @lc code=end
