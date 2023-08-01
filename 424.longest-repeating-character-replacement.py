#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

from collections import Counter


# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # get a substring
        # knowing how many switch is needed

        maxLength, start, end = 0, 0, 1
        hash = dict()

        while start < end and end <= len(s):
            if s[end - 1] in hash:
                hash[s[end - 1]] += 1
            else:
                hash[s[end - 1]] = 1
            maxLetter = max(hash.values())
            if len(s[start:end]) - maxLetter > k:
                hash[s[start]] -= 1
                start += 1
                end += 1

            else:
                maxLength = max(maxLength, len(s[start:end]))
                end += 1

        return maxLength

        # @lc code=end
