#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#


# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        val = 0
        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                val = max(val, len(citations) - i)
        return val


# @lc code=end
