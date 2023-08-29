#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left = self.maxDepth(root.left) if root.left else 0
            right = self.maxDepth(root.right) if root.right else 0
            # need to +1 to indicate it is a different level
            return max(left, right) + 1
        return 0


# @lc code=end
