#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # the curve looks like /\/
            # the left half of the array is all /
            if nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the right half of the array dont have the second \
            elif nums[mid] >= target >= nums[r]:
                l = mid + 1
            # the right half of the array is all /
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1


# @lc code=end
