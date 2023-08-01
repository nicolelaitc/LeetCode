#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while len(stack) > 0:
                if stack[-1][0] < temperatures[i]:
                    index = stack[-1][1]
                    ans[index] = i - index
                    stack.pop()
                else:
                    break

            stack.append((temperatures[i], i))

        return ans

        # @lc code=end
