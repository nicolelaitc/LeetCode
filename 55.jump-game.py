#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = 0
        for i in range(len(nums)):
            if i > p:
                return False
            p = max(p, i + nums[i])
        return True


# @lc code=end
