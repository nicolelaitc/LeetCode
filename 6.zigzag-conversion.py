#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#


# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        seq = [n for n in range(numRows)] + [n for n in range(numRows - 2, 0, -1)]
        for i, c in enumerate(s):
            rowNum = i % len(seq)
            rows[seq[rowNum]] += c
        return "".join(rows)


# @lc code=end
