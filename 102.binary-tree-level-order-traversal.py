#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [[root]]
        ans = [[root.val]]
        while len(queue) > 0:
            li = queue.pop(0)
            temp = []
            tempNode = []
            for node in li:
                if node.left:
                    tempNode.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    tempNode.append(node.right)
                    temp.append(node.right.val)
            if len(temp) > 0:
                ans.append(temp)
                queue.append(tempNode)

        return ans


# @lc code=end
