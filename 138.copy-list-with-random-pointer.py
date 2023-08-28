#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        hashMap = dict()
        if not head:
            return None
        start = Node(head.val)
        hashMap[head] = start
        newHead = start

        while head and newHead:
            newHead = hashMap.setdefault(head, Node(head.val))
            next = (
                hashMap.setdefault(head.next, Node(head.next.val))
                if head.next
                else None
            )
            random = (
                hashMap.setdefault(head.random, Node(head.random.val))
                if head.random
                else None
            )

            newHead.next = next
            newHead.random = random

            newHead = newHead.next
            head = head.next

        return start
        # if head not in hashMap:
        #     newHead = self.Node(head.val)
        #     hashMap[head] = newHead
        # else:
        #     newHead = hashMap[head]
        # if head.Next not in hashMap:
        #     next = self.Node(head.next.val)
        # if


# @lc code=end
