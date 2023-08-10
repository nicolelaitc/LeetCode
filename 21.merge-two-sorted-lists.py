#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if not list1 and not list2:
            return None
        head, tail = list1, list1
        current1, current2 = list1, list2

        if list1.val > list2.val:
            head, tail = list2, list2
            current1, current2 = list1, list2.next
        else:
            current1, current2 = list1.next, list2

        while current1 and current2:
            if current1.val < current2.val:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        if current1:
            tail.next = current1
        if current2:
            tail.next = current2

        print(head, tail, current1, current2)

        return head


# @lc code=end
