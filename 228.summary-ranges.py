#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#


# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ans = list()
        p1, p2 = 0, 0
        while p2 < len(nums):
            if (nums[p2] - nums[p1]) == p2 - p1:
                p2 += 1
            else:
                if p2 - p1 == 1:
                    ans.append(str(nums[p1]))
                else:
                    print(p1, p2)
                    ans.append(str(nums[p1]) + "->" + str(nums[p2 - 1]))
                p1 = p2

        if p2 - p1 == 1:
            ans.append(str(nums[p1]))
        else:
            ans.append(str(nums[p1]) + "->" + str(nums[p2 - 1]))

        return ans


# @lc code=end
