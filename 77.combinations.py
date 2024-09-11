#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtracking(list: list[int], n: int):
            if list[-1] < n and (n - list[-1]) > k - len(list):
                return list[:-1] + [list[-1] + 1]
            else:
                l = backtracking(list[:-1], n)
                return l + [l[-1] + 1]

        ans = [[x for x in range(1, k + 1)]]
        while ans[-1][0] < n - k + 1:
            ans.append(backtracking(ans[-1], n))

        return ans


# @lc code=end
