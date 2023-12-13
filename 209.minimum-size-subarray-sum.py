#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#


# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] >= target:
            return 1
        min_length = float("inf")
        start, end, current_sum = 0, 0, 0

        # find the array that sums equal or greater than x first
        while end < len(nums):
            if nums[end] >= target:
                return 1
            current_sum = current_sum + nums[end]
            end = end + 1

            while start < end and current_sum >= target:
                current_sum = current_sum - nums[start]
                start = start + 1

                min_length = min(min_length, end - start + 1)

        return min_length if min_length != float("inf") else 0


# @lc code=end
