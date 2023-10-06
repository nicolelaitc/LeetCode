#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        res = 0
        l = 0

        while l < len(height)-1 and height[l+1] >= height[l]:
            l += 1
        r = l + 2

        while r < len(height):
            if height[r] == 0 or l+1 >= r:
                r += 1
                continue
            if height[l] == 0 or height[l+1] >= height[l]:
                l += 1
                continue
            if height[l] > height[r]:
                if height[r] != max(height[r:]):
                    r += 1
                    continue
            tmp = min(height[r], height[l])
            #tmp = min(height[r], height[l])*(r-l-1) - sum(height[l+1:r])
            res += sum(tmp - n for n in height[l+1:r] if tmp > n)
            l = r
            r = l + 2

        return res


# @lc code=end
