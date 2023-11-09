#
# @lc app=leetcode id=1759 lang=python3
#
# [1759] Count Number of Homogenous Substrings
#


# @lc code=start
class Solution:
    def countHomogenous(self, s: str) -> int:
        # break it into list of homogenous strings first
        current_str, current_head = s[0], s[0]
        l = []

        for c in s[1:]:
            if c == current_head:
                current_str += c
            else:
                l.append(current_str)
                current_str = c
                current_head = c
        l.append(current_str)

        print(l)

        f = dict()
        res = 0

        for h in l:
            len_h = len(h)
            if len_h not in f:
                f[len_h] = len_h * (len_h + 1) // 2
            res += f[len_h]
        print(f)

        return res % (10**9 + 7)


# @lc code=end
