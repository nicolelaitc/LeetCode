#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.right:
            return self.leftFirst(root.left) == self.rightFirst(root.right)
        return root.left == root.right

    def leftFirst(self, root: Optional[TreeNode]) -> list:
        if not root:
            return ["null"]
        return [root.val] + self.leftFirst(root.left) + self.leftFirst(root.right)

    def rightFirst(self, root: Optional[TreeNode]) -> list:
        if not root:
            return ["null"]
        return [root.val] + self.rightFirst(root.right) + self.rightFirst(root.left)


# @lc code=end
