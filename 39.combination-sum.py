#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> List[List[int]]:
        arr = [[x] for x in candidates]
        ans = []

        while len(arr) > 0:
            l = arr.pop(0)
            diff = target - sum(l)
            if diff == 0:
                ans.append(l)
            for x in candidates:
                if l[-1] <= x:
                    if diff > x:
                        arr.append(l + [x])
                    elif diff == x:
                        ans.append(l + [x])

        return ans


# @lc code=end
