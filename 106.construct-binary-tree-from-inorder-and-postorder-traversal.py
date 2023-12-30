#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        # split the array to left, right, and main
        root = TreeNode(postorder[-1])
        midindex = inorder.index(postorder[-1])
        rightindex = len(postorder) - len(inorder[midindex + 1 :]) - 1
        # rightIndex = (
        #     postorder.index(inorder[midindex])
        #     if len(inorder) > midindex
        #     else len(postorder) - 2
        # )
        root.left = self.buildTree(inorder[:midindex], postorder[:rightindex])
        root.right = self.buildTree(inorder[midindex + 1 :], postorder[rightindex:-1])
        return root


# @lc code=end
