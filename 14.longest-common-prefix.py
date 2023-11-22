#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        for i in reversed(range(len(strs[0]))):
            prefix = strs[0][: i + 1]
            ok = True
            for s in strs[1:]:
                if not s.startswith(prefix):
                    ok = False
                    break
            if ok == True:
                return prefix

        return ""


# @lc code=end
