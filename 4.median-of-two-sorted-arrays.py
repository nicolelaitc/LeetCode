#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#


# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # from Neetcode
        # binary search for the shortest arrays
        a, b = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        l, r = 0, len(a) - 1
        # the half of the total length of the combined array
        half = (len(a) + len(b)) // 2

        while True:
            i = (l + r) // 2
            j = half - i - 2
            # aLeft + bLeft should include all the left side of combined array
            Aleft = a[i] if i >= 0 else float("-inf")
            Aright = a[i + 1] if (i + 1) < len(a) else float("inf")
            Bleft = b[j] if j >= 0 else float("-inf")
            Bright = b[j + 1] if (j + 1) < len(b) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(a) + len(b)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1


# @lc code=end
