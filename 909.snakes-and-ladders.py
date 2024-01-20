#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#


# @lc code=start
from collections import deque


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()

        def intToPos(num):
            quotient = (num - 1) // length
            remainder = (num - 1) % length
            if quotient % 2 == 0:
                return (quotient, remainder)
            else:
                return (quotient, length - remainder - 1)

        q = deque()
        q.append([1, 0])
        visit = set()
        while q:
            curr, step = q.popleft()
            if curr == length * length:
                return step
            for i in range(1, 7):
                next = curr + i

                r, c = intToPos(next)
                if board[r][c] != -1:
                    next = board[r][c]
                if next == length * length:
                    return step + 1
                if next not in visit:
                    visit.add(next)
                    q.append([next, step + 1])

        return -1


# @lc code=end
