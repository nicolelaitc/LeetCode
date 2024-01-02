#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
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
        if root is None:
            return None

        # pathfinding?
        stack = [[root]]
        path = []
        while stack:
            nodeList = stack.pop()
            if nodeList[-1] == p or nodeList[-1] == q:
                path.append(nodeList)
            if nodeList[-1].left:
                stack.append(nodeList + [nodeList[-1].left])
            if nodeList[-1].right:
                stack.append(nodeList + [nodeList[-1].right])

        print(len(path))

        # find the intersection
        common = set(path[0]).intersection(set(path[1]))

        for i in range(-1, -max(len(path[0]), len(path[1])) - 1, -1):
            if path[0][i] in common:
                return path[0][i]
            elif path[1][i] in common:
                return path[1][i]

        return root


# @lc code=end
