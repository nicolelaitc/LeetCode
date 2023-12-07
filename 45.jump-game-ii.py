#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # we check the distance that can reach from curr_start, and then comparing every node within the distance that who can go longest, and then next time start from that
        curr_longest, curr_end, count = 0, 0, 0
        for i in range(len(nums) - 1):
            if i + nums[i] >= len(nums) - 1:
                return count + 1
            curr_longest = max(curr_longest, i + nums[i])
            if i == curr_end:
                curr_end = curr_longest
                count += 1

        return count


# @lc code=end
