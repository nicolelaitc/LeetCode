#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # find the overlapping area?
        points.sort()
        arrow = []
        for i in range(len(points)):
            if arrow:
                overlap = self.find_overlap(arrow[-1], points[i])
                if overlap:
                    arrow[-1] = overlap
                else:
                    arrow.append(points[i])
            else:
                arrow.append(points[i])

        print(arrow)
        return len(arrow)

    def find_overlap(self, interval1, interval2):
        # Find the maximum of the start points
        start = max(interval1[0], interval2[0])
        # Find the minimum of the end points
        end = min(interval1[1], interval2[1])

        # Check if there is an overlap
        if start <= end:
            return [start, end]
        else:
            return []  # No overlap
