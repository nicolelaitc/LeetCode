#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            start, end = intervals[i]
            if start <= intervals[i - 1][1]:
                intervals[i][0] = intervals[i - 1][0]
                intervals[i][1] = max(intervals[i - 1][1], end)
                intervals.pop(i - 1)
            else:
                i += 1
        return intervals


# @lc code=end
