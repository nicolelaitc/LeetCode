#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = 0
        ans = ""

        if s == s[::-1]:
            return s

        l, r = 0, 0
        while r <= len(s):
            if s[l:r] == s[l:r][::-1]:
                if max < len(s[l:r]):
                    max = len(s[l:r])
                    ans = s[l:r]
            if r == len(s):
                l += 1
                r = l
            else:
                r += 1

        return ans


# @lc code=end
