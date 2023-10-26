#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = []

        arr += self.PathSum(root)
        print(arr)
        return max(arr)

    def PathSum(self, root: Optional[TreeNode]) -> [int, int]:
        if root is None:
            return 0
        left, leftSub, right, rightSub = (
            float("-inf"),
            float("-inf"),
            float("-inf"),
            float("-inf"),
        )
        if root.left:
            left, leftSub = self.PathSum(root.left)
        if root.right:
            right, rightSub = self.PathSum(root.right)
        r = root.val

        print(
            f"root: {r}, left: {left}, right: {right}, leftSub: {leftSub}, rightSub: {rightSub}"
        )

        return [
            # for keep checking the branch
            max(r + left, r + right, r),
            # for the node/sub-tree that do not need 3extra adding
            max(r + left + right, leftSub, rightSub, left, right),
        ]

        # left = self.maxPathSum(root.left) if root.left else float("-inf")
        # right = self.maxPathSum(root.right) if root.right else float("-inf")
        # r = root.val
        # print(
        #     f"r: {r}, r + left: {r + left}, r + right: {r + right}, r + left + right: {r + left + right}, , left: {left}, right: {right}"
        # )
        # return max(r, r + left, r + right, r + left + right, left, right)


# @lc code=end
