#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        p = 0
        count = 0
        while len(nums) > 1:
            if nums[0] >= len(nums) - 1:
                return count + 1
            arr = [n + i for i, n in enumerate(nums[1 : nums[0] + 1])]
            maxVal = max(arr)
            print(f"arr={arr}, maxVal={maxVal}")
            p = arr.index(maxVal) + 1
            count += 1
            nums = nums[p:]
        return count

        # while p < len(nums) - 1:
        #     if (p + nums[p]) >= len(nums) - 1:
        #         return count + 1
        #     arr = nums[p + 1 : p + nums[p] + 1]
        #     print(arr)
        #     maxVal = max(arr)
        #     p = nums.index(maxVal)
        #     count += 1
        #     print(f"p: {p}")
        #     nums = nums[p:]
        # return count


# @lc code=end
