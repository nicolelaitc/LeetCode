#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for key in counts:
            while counts[key] > 2:
                nums.remove(key)
                counts[key] -= 1
        return len(nums)


# @lc code=end
