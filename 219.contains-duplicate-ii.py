#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        if len(set(nums)) == len(nums):
            return False
        i, j = 0, min(k, len(nums) - 1)
        while j < len(nums):
            arr = nums[i : j + 1]
            if len(set(arr)) != len(arr):
                return True
            i += 1
            j += 1
            # print(i, j)
        return False


# @lc code=end
