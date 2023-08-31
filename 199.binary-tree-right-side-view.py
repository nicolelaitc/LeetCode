#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodeList = []
        if not root:
            return nodeList
        if root:
            nodeList = [[root]]
            p = 0
            while p < len(nodeList):
                # the node in the same layer belongs to the list in the same index
                li = nodeList[p]
                temp = []
                for node in li:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                if len(temp) > 0:
                    nodeList.append(temp)
                p += 1

            ans = [p[-1].val for p in nodeList]
            return ans


# @lc code=end
