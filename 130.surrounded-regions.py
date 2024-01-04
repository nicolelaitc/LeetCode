#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#


# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board[0] = ["D" if x == "O" else x for x in board[0]]
        board[-1] = ["D" if x == "O" else x for x in board[-1]]
        for row in board:
            if row[0] == "O":
                row[0] = "D"
            if row[-1] == "O":
                row[-1] = "D"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "D":
                    self.dfs(board, i + 1, j)
                    self.dfs(board, i - 1, j)
                    self.dfs(board, i, j + 1)
                    self.dfs(board, i, j - 1)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "D":
                    board[i][j] = "O"

    def dfs(self, board, i, j):
        if (
            i < 0
            or i >= len(board)
            or j < 0
            or j >= len(board[0])
            or board[i][j] == "X"
            or board[i][j] == "D"
        ):
            return

        # make all the adjacent cells to be "D"
        if board[i][j] == "O":
            board[i][j] = "D"
        self.dfs(board, i + 1, j)
        self.dfs(board, i - 1, j)
        self.dfs(board, i, j + 1)
        self.dfs(board, i, j - 1)


# @lc code=end
