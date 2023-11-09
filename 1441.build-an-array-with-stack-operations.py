#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#


# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stream = [x for x in range(1, n + 1)]
        stack = []
        p = 0
        ans = []
        while stack != target:
            if stream[p] == target[p]:
                ans.append("Push")
                stack.append(stream[p])
                p += 1

            else:
                ans.append("Push")
                ans.append("Pop")
                stream.pop(p)

        return ans


# @lc code=end
