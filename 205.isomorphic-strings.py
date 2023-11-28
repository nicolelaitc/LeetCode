#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                if t[i] in hash.values():
                    return False
                hash[s[i]] = t[i]
            else:
                if hash[s[i]] != t[i]:
                    return False

        return True


# @lc code=end
