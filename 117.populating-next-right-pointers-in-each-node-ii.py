#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        queue = [root]
        while queue:
            arr = []
            for i in range(len(queue)):
                if i < len(queue) - 1:
                    queue[i].next = queue[i + 1]
                if queue[i].left:
                    arr.append(queue[i].left)
                if queue[i].right:
                    arr.append(queue[i].right)
            queue = arr

        return root


# @lc code=end
