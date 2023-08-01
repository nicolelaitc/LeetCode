#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join(item.lower()
                     for item in s if item.isalnum() == True)
        print(ns, ns[::-1])
        if ns == ns[::-1]:
            return True

        return False

        # @lc code=end
