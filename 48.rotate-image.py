#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#


# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        n = len(matrix)
        while i < n:
            arr = [matrix[r].pop(0) for r in range(n)][::-1]
            matrix.append(arr)
            i += 1

        while True:
            if len(matrix) == n:
                break
            matrix.pop(0)


# @lc code=end
