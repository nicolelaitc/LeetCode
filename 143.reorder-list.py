#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle of list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = self.reverseList(slow.next)
        slow.next = None
        # merge
        while head and second:
            hNext = head.next
            head.next = second
            head = second
            second = hNext

        return

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # (nil) -> 1 - > 2 - > 3
        prev = None
        current = head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        return prev


# @lc code=end
