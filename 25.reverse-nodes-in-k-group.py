#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# inspired by NeetCode
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev, start = dummy, dummy

        while True:
            groupLast = self.getKth(groupPrev, k)
            if start == dummy:
                start = groupLast
            if groupLast is None:
                break
            groupPrev = self.reverse(groupPrev, groupLast, k)
        return start

    def getKth(self, head, k):
        while k > 0 and head:
            head = head.next
            k -= 1
        return head

    def reverse(self, groupPrev, end, k):
        groupNext = end.next
        current = groupPrev.next
        groupEnd = current
        prev = None
        while current and k > 0:
            next = current.next
            current.next = prev
            prev = current
            current = next
            k -= 1

        groupPrev.next = end
        groupEnd.next = groupNext
        return groupEnd


# [1,7,3,2,7,0,1,0,0]\n 4
# @lc code=end
