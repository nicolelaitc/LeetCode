#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        stack = []
        sortedArr = []
        current = root

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left
            current = stack.pop()
            sortedArr.append(current.val)
            current = current.right

        return sortedArr[k - 1]


# @lc code=end
