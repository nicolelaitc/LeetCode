#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#


# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        stack = [x for x in stack if x != "" and x != "."]
        p = 0
        while stack and p < len(stack):
            if stack[p] in (".", "/", ""):
                stack.pop(p)
                print(1)
            elif stack[p] == "..":
                stack.pop(p)
                if p > 0:
                    stack.pop(p - 1)
                p -= 1 if p > 0 else 0
                print(2)
            else:
                p += 1
                print(3)
            print(stack, p)
        return "/" + "/".join(stack)


# @lc code=end
