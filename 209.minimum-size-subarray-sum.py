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
        left, right, res = 0, 0, float("inf")
        curr_sum = nums[left]

        while right + 1 < len(nums):
            right += 1
            curr_sum += nums[right]
            if nums[right] >= target:
                return 1

            while left <= right and curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return res if res != float("inf") else 0


# @lc code=end
