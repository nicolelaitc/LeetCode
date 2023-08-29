#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        if root.val == subRoot.val:
            res = self.isSameTree(root, subRoot)
        if res:
            return res

        left, right = False, False
        if root.left:
            left = self.isSubtree(root.left, subRoot)
        if root.right:
            right = self.isSubtree(root.right, subRoot)
        res = any([left, right])
        return res

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (p and not q) or (not p and q):
            return False
        if p.val != q.val:
            return False

        if p.left and q.left:
            left = self.isSameTree(p.left, q.left)
        elif not p.left and not q.left:
            left = True
        else:
            left = False

        if p.right and q.right:
            right = self.isSameTree(p.right, q.right)
        elif not p.right and not q.right:
            right = True
        else:
            right = False

        return all([left, right])


# @lc code=end
