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
        return self.dfs(root, 0)

    def dfs(self, root, path):
        if not root:
            return 0
        path = path * 10 + root.val
        if not root.left and not root.right:
            return path
        return self.dfs(root.left, path) + self.dfs(root.right, path)


# @lc code=end
