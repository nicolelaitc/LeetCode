#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [[x for x in range(1, n + 1)]]
        ans = [[x] for x in range(1, n - k + 2)]
        while len(ans[0]) < k and ans[0][0] <= n:
            l = ans.pop(0)
            if l[-1] < n:
                for x in range(l[-1] + 1, n + 1):
                    ans.append(l + [x])
        return ans


# @lc code=end
