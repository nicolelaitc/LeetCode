#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if len(s) > len(t):
            return False

        ps, pt = 0, 0
        while ps < len(s) and pt < len(t) and len(t) >= len(s):
            if t.startswith(s):
                return True
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                t = t[:pt] + t[pt + 1 :]

        return False


# @lc code=end
