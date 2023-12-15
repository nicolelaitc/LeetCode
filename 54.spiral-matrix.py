#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            # right
            ans += matrix.pop(0)
            if matrix:
                # down
                for row in matrix:
                    if row:
                        ans.append(row.pop(-1))
            if matrix:
                ans += matrix.pop(-1)[::-1]
            if matrix:
                for row in matrix[::-1]:
                    if row:
                        ans.append(row.pop(0))
        return ans


# @lc code=end
