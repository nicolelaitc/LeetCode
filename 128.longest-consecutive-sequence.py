#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        answer = 0
        for num in nums_set:
            if num-1 not in nums_set:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                answer = max(answer, length)
        return answer

        # @lc code=end
