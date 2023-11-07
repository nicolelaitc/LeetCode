#
# @lc app=leetcode id=1921 lang=python3
#
# [1921] Eliminate Maximum Number of Monsters
#


# @lc code=start
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = sorted([dist[i] / speed[i] for i in range(len(dist))])

        p = 0
        while p < len(arrival_time):
            if arrival_time[p] > p:
                p += 1
            else:
                break

        return p

        # shooting_time, monster_total = 0, len(dist)

        # while shooting_time < monster_total:
        #     shooting_time += 1
        #     dist = [d - s for d, s in zip(dist, speed)]
        #     arrived = sum(d <= 0 for d in dist)
        #     # print(f"dist: {dist}, arrived: {arrived}, shooting: {shooting_time}")
        #     if arrived > shooting_time:
        #         return shooting_time


# @lc code=end
