#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # compare the mid point with the first element so we know the flow
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # if mid < first, meaning the max point is between l and mid
            if nums[mid] > nums[mid + 1]:
                print(nums[mid], nums[mid + 1])
                return nums[mid + 1]
            elif nums[mid] < nums[l]:
                r = mid
            else:
                l = mid + 1
            print(l, r, mid)

        return nums[0]


# @lc code=end
