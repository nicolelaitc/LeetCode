#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1

        while i < j and j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1

        return i + 1


# @lc code=end
