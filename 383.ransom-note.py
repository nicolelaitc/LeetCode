#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for l in ransomNote:
            if l not in magazine:
                return False
            magazine = magazine.replace(l, "", 1)
        return True


# @lc code=end
