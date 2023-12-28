#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head.next or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        leftNode = dummy

        for _ in range(left - 1):
            leftNode = leftNode.next  # 2

        curr = leftNode.next  # 3
        for _ in range(left, right):
            temp = curr.next  # 4
            curr.next = temp.next  # 5
            temp.next = leftNode.next  # 3
            leftNode.next = temp  # 4

        return dummy.next


# @lc code=end
