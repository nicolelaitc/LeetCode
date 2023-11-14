#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # i = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         nums.remove(val)
        #     else:
        #         i += 1

        # return len(nums)

        count = nums.count(val)
        while count > 0:
            nums.remove(val)
            count -= 1
        return len(nums)


# @lc code=end
