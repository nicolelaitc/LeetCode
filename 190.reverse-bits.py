#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            bit = (n >> i) & 1  # Extract the ith bit of n
            result |= bit << (
                31 - i
            )  # Shift the bit to its reverse position and OR it with the result
        return result


# @lc code=end
