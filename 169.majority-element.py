#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        keys = list(set(nums))
        for key in keys:
            if nums.count(key) > len(nums) / 2:
                return key


# @lc code=end
