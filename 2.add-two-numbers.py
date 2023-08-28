#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = ListNode(0)
        start = ans

        while (l1 or l2) and ans:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            val = a + b + ans.val
            if val >= 10:
                ans.val = val - 10
                ans.next = ListNode(1)
            else:
                ans.val = val

            l1 = l1.next if (l1 and l1.next) else None
            l2 = l2.next if (l2 and l2.next) else None
            if (l1 or l2) and ans.next is None:
                ans.next = ListNode(0)
            ans = ans.next if (l1 or l2) else None

        return start


# @lc code=end
