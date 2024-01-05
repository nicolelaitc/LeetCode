#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None
        created = dict()
        start, curr = None, [node]

        while curr:
            now = curr.pop()
            # create node for
            copy_curr = created.get(now.val, Node(val=now.val))
            for n in now.neighbors:
                created[n.val] = created.get(n.val, Node(val=n.val))
                if not created[n.val].neighbors:
                    curr.append(n)
                if created[n.val] not in copy_curr.neighbors:
                    copy_curr.neighbors.append(created[n.val])

            created[copy_curr.val] = copy_curr

            if not start:
                start = copy_curr

        return start

        # save node.neighbour in neighbour

        #


# @lc code=end
