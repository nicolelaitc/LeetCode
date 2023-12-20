#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#


# @lc code=start
class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        left = [l for l in intervals if l[1] < newInterval[0]]
        right = [r for r in intervals if r[0] > newInterval[1]]
        print(left, right)

        if left + right != intervals:
            newInterval = [
                min(intervals[len(left)][0], newInterval[0]),
                max(intervals[-len(right) - 1][1], newInterval[1]),
            ]

        return left + [newInterval] + right


# @lc code=end
