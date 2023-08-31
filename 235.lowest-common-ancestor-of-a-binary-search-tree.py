#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if not root:
            return None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        leftVal = left.val if left else None
        rightVal = right.val if right else None

        valList = [root.val, leftVal, rightVal]

        if p.val in valList and q.val in valList:
            return root

        if leftVal is not None and rightVal is None:
            return left
        if rightVal is not None and leftVal is None:
            return right
        if root.val == p.val:
            return p
        if root.val == q.val:
            return q

        return None
        # @lc code=end
