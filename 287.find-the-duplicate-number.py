#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#


# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = len(nums) * [0]
        for num in nums:
            if arr[num] == 1:
                return num
            arr[num] = 1


# @lc code=end
