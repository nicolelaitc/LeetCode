#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        arr = []

        def insert(i, j, l):
            nonlocal arr
            if [i, j] not in l:
                arr.insert(0, l + [[i, j]])

        def search(l: list[int]):
            i, j = l[-1][0], l[-1][1]
            c = word[len(l)]
            if i > 0 and board[i - 1][j] == c:
                insert(i - 1, j, l)
            if j > 0 and board[i][j - 1] == c:
                insert(i, j - 1, l)
            if i < len(board) - 1 and board[i + 1][j] == c:
                insert(i + 1, j, l)
            if j < len(board[0]) - 1 and board[i][j + 1] == c:
                insert(i, j + 1, l)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    arr.append([[i, j]])
                    while len(arr) > 0:
                        l = arr.pop(0)
                        if len(l) == len(word):
                            return True
                        search(l)

        return False


# @lc code=end
