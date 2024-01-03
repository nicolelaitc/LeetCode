#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue

                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    visited = self.check(grid, i, j, visited)

                visited.add((i, j))

        return island

    def check(self, grid, i, j, visited):
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x == i or y == j:
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            if (x, y) not in visited:
                                visited.add((x, y))
                                if grid[x][y] == "1":
                                    stack.append((x, y))

        return visited


# @lc code=end
