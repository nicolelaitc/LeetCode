#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#


# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        check = []
        board.reverse()
        for n in range(len(board)):
            if n % 2 == 1:
                board[n].reverse()
        if board[-1][-1] != -1:
            return -1
        print(board)
        for _ in range(len(board)):
            check.append([float("inf")] * len(board[0]))
        check[0][0] = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                step = check[i][j] + 1
                for k in range(1, 7):
                    newDest = self.destination(board, [i, j], k)
                    if newDest == []:
                        print(check[-1][-1], step)
                        check[-1][-1] = min(check[-1][-1], step)
                    else:
                        check[newDest[0]][newDest[1]] = min(
                            check[newDest[0]][newDest[1]], step
                        )

        print(check)
        return check[-1][-1] if check[-1][-1] != float("inf") else -1

    def destination(self, board, last, dice):
        i, j = last[0], last[1]
        j += dice
        while j > len(board[0]) - 1:
            i += 1
            j -= len(board[0])

        if i > len(board) - 1:
            return []

        if board[i][j] != -1:
            i, j = (board[i][j] // len(board[0])), (board[i][j] % len(board[0])) - 1
            if j == -1:
                j = len(board[0]) - 1
                i -= 1
        return [i, j]


# @lc code=end
