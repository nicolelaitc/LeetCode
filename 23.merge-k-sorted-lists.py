#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # record the pointer
        arr = []
        for node in lists:
            if node is not None:
                arr.append(node)

        if len(arr) == 0:
            return None
        elif len(arr) == 1:
            return arr[0]

        start, head = None, None

        while len(arr) > 0:
            p_min, val_min = 0, float("inf")
            for i in range(len(arr)):
                if arr[i] != float("inf"):
                    if arr[i].val < val_min:
                        p_min = i
                        val_min = arr[i].val

            if head is None:
                head = arr[p_min]
                start = head
            else:
                head.next = arr[p_min]
                head = head.next
            if arr[p_min].next:
                arr[p_min] = arr[p_min].next
            else:
                # the linked list is exhausted
                arr.pop(p_min)

        return start


# @lc code=end
