#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        num = 0
        stack = [[root]]
        while stack:
            nodeList = stack.pop()
            if not nodeList[-1].left and not nodeList[-1].right:
                num += int("".join([str(i.val) for i in nodeList]))
            if nodeList[-1].left:
                stack.append(nodeList + [nodeList[-1].left])
            if nodeList[-1].right:
                stack.append(nodeList + [nodeList[-1].right])

        return num


# @lc code=end
