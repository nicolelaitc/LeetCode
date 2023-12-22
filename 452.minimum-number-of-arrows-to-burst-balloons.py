#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # find the overlapping area?
        points.sort(key=lambda x: x[1])
        tally, bow = 1, points[0][1]
        for start, end in points:
            if start > bow:
                tally += 1
                bow = end

        return tally
