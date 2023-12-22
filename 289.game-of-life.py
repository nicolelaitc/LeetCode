#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#


# @lc code=start


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        live, dead = list(), list()
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = self.count_live_cells(board, i, j)
                if board[i][j] == 0 and count == 3:
                    live.append([i, j])
                elif board[i][j] == 1 and (count < 2 or count > 3):
                    dead.append([i, j])

        print(live, dead)

        for i, j in live:
            board[i][j] = 1
        for i, j in dead:
            board[i][j] = 0

    def count_live_cells(self, board, i, j) -> int:
        count = 0
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    count += board[x][y]
        # print(f"i={i}, j={j}, count={count}")
        return count - board[i][j]


# @lc code=end
