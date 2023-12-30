#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        beforePart = dummy
        while beforePart.next:
            if beforePart.next.val < x:
                beforePart = beforePart.next
            else:
                break

        curr = beforePart
        while curr.next:
            if curr.next.val < x:
                currNextNext = curr.next.next  # None
                beforePartNext = beforePart.next  # 4
                beforePart.next = curr.next  # 2 -> 2
                beforePart = beforePart.next  # 2
                beforePart.next = beforePartNext  # 2 -> 4
                curr.next = currNextNext  # 5 -> None
            else:
                curr = curr.next

        return dummy.next


# @lc code=end
