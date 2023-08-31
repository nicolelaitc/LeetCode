#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        return len(self.checkSubTree(root)) > 0

    def checkSubTree(self, root: Optional[TreeNode]) -> list[int]:
        ans = [root.val]
        if root.left:
            left = self.checkSubTree(root.left)
            if len(left) == 0:
                return []
            if root.val <= max(left):
                return []
            ans += left
        if root.right:
            right = self.checkSubTree(root.right)
            if len(right) == 0:
                return []
            if root.val >= min(right):
                return []
            ans += right
        return ans


# @lc code=end
