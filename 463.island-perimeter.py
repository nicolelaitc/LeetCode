#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        answer = 0

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    # left
                    if j == 0 or row[j - 1] == 0:
                        answer += 1
                    # right
                    if j == len(row) - 1 or row[j + 1] == 0:
                        answer += 1
                    if i == 0 or grid[i - 1][j] == 0:
                        answer += 1
                    if i == len(grid) - 1 or grid[i + 1][j] == 0:
                        answer += 1

        return answer


# @lc code=end
