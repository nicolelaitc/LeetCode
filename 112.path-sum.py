#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root:
            stack = [root]
            while stack:
                node = stack.pop(-1)
                if node.val == targetSum and not node.left and not node.right:
                    return True
                if node.left:
                    node.left.val += node.val
                    stack.append(node.left)
                if node.right:
                    node.right.val += node.val
                    stack.append(node.right)

        return False


# @lc code=end
