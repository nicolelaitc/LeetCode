#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        curr, end = head, None
        while curr:
            if not curr.next:
                end = curr
                break
            curr = curr.next

            length += 1

        if k % length == 0:
            return head
        curr, newHead = head, None

        # remainder : in the middle
        # remainder : in the end (rotate k - 1)

        rotation = length - (k % length)
        while rotation > 0:
            if rotation == 1:
                newHead = curr.next if curr.next else curr
                curr.next = None
            else:
                curr = curr.next
            rotation -= 1

        end.next = head
        return newHead


# @lc code=end
