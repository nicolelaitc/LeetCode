#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#


# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_hash, column_hash = list(), list()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_hash.append(i)
                    column_hash.append(j)
        print(row_hash, column_hash)

        for i in row_hash:
            matrix[i] = [0] * len(matrix[0])
        for j in column_hash:
            for i in range(len(matrix)):
                matrix[i][j] = 0


# @lc code=end
