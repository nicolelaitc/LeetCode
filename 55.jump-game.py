#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#


# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        arr = [True] + [False] * (len(nums) - 1)
        # exhaust all the possibilities
        for n in range(len(nums)):
            if arr[n]:
                for i in range(n, n + nums[n] + 1):
                    if i < len(nums):
                        arr[i] = True
            if arr[-1]:
                return True
        print(arr)

        return False


# @lc code=end
