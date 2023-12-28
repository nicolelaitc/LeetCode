#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr and curr.next:
            if curr.val == curr.next.val:
                while curr.next.next:
                    if curr.next.next.val == curr.val:
                        curr.next.next = curr.next.next.next
                    else:
                        break
                if prev:
                    prev.next = curr.next.next if curr.next.next else None
                    curr = prev
                else:
                    head = curr.next.next if curr.next.next else None
                    curr = head
            else:
                prev = curr
                curr = curr.next

        return head


# @lc code=end
