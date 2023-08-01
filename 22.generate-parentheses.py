#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = [["", n, n]]
        answer = []
        while len(stack) > 0:
            curr = stack.pop(0)
            string = curr[0]
            open_count = curr[1]
            close_count = curr[2]
            # if the array can add close
            if close_count > open_count:
                stack.append([string + ")", open_count, close_count - 1])
            # if the array can still add open
            if open_count > 0:
                stack.append([string+"(", open_count-1, close_count])

            if open_count <= 0 and close_count <= 0:
                answer.append(string)

        return answer


# @lc code=end
