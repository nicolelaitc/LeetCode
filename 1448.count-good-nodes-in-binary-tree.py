#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS? Pathfinding?
        p = 0
        stack = [root]
        valStack = [[root.val]]
        while p < len(stack):
            node = stack[p]
            val = valStack[p]
            if node.left:
                stack.append(node.left)
                valStack.append(val + [node.left.val])
            if node.right:
                stack.append(node.right)
                valStack.append(val + [node.right.val])
            p += 1

        return len([x for x in valStack if max(x) == x[-1]])


# @lc code=end
