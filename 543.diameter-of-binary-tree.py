#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # add up the max depth of the left and max depth of the right tree
        # save the number for every result returned
        ans = self.diameterOfNode(root, 0)
        return ans

    def diameterOfNode(self, root: Optional[TreeNode], maxVal: int) -> int:
        # add up the max depth of the left and max depth of the right tree
        # save the number for every result returned
        left = self.diameterOfNode(root.left, maxVal) if root.left else 0
        right = self.diameterOfNode(root.right, maxVal) if root.right else 0
        return max(self.maxDepth(root.left) + self.maxDepth(root.right), left, right)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left = self.maxDepth(root.left) if root.left else 0
            right = (
                self.maxDepth(
                    root.right,
                )
                if root.right
                else 0
            )
            # need to +1 to indicate it is a different level
            return max(left, right) + 1
        return 0


# @lc code=end
