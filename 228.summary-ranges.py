#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        for n in nums:
            if not ranges or ranges[-1][1] + 1 != n:
                ranges.append([n, n])
            else:
                ranges[-1][1] = n
        return [f"{x}->{y}" if x != y else f"{x}" for x, y in ranges]


# @lc code=end
