#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for p in path:
            if p == "..":
                if stack:
                    stack.pop()
            elif p not in ["", "."]:
                stack.append(p)
        return "/" + "/".join(stack)


# @lc code=end
