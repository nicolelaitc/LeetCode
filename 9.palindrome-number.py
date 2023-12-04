#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            ans = 0
            start = x
            while x > 0:
                ans = ans * 10 + x % 10
                x //= 10

        return ans == start


# @lc code=end
