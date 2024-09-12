#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = [[nums[0]]]
        if len(nums) == 1:
            return ans
        for i in range(1, len(nums)):
            targetInt = nums[i]
            while len(ans[0]) < i + 1:
                l = ans.pop(0)
                for x in range(0, (i + 1)):
                    newArr = l.copy()
                    newArr.insert(x, targetInt)
                    ans.append(newArr)

        return ans


# @lc code=end
