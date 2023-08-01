#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ["{", "[", "("]
        close = ["}", "]", ")"]
        for item in s:
            if item in open:
                stack.append(item)
            else:
                try:
                    tmp = stack.pop()
                except IndexError:
                    return False
                if open.index(tmp) != close.index(item):
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

            # @lc code=end
