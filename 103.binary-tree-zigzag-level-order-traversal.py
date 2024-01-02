#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        stack, p = [[root]], 0
        # use boolean to determine the direction of traversal
        direction = False
        while p < len(stack):
            layer = stack[p]
            l = list()
            for node in layer:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            if l:
                stack.append(l)
            p += 1
        print(stack)
        ans = []
        while stack:
            l = stack.pop(0)
            if direction:
                l.reverse()
            direction = not direction
            ans.append([node.val for node in l])

        return ans


# @lc code=end
