#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#


# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        start, end = 1, k + 1
        res = [max(nums[start - 1 : end - 1])]
        while end <= len(nums):
            if nums[end - 1] >= res[-1]:
                res.append(nums[end - 1])
                pass
            # if max is removed
            elif nums[start - 1] == res[-1]:
                res.append(max(nums[start:end]))
                pass
            # if the end is bigger
            # it needs to be n - 1 since we use [start:end]

            else:
                res.append(res[-1])
            start += 1
            end += 1

        return res
        """

        # deque
        # O(n) time, O(k) space
        from collections import deque

        # it is used to save the index of the element
        indexes = deque()
        res = []
        for i, num in enumerate(nums):
            # remove the first element if it's out of the window
            if indexes and indexes[0] == i - k:
                indexes.popleft()
            # remove the element which is smaller than the current element
            while indexes and nums[indexes[-1]] < num:
                indexes.pop()
            indexes.append(i)
            # keep appending the largest until it is removed by the if loop before
            if i >= k - 1:
                res.append(nums[indexes[0]])
        return res

        # monotonic queue
        # O(n) time, O(k) space
        # monotonic queue is a queue that only keeps increasing order
        # if the queue is empty, we can always append the element
        # if the queue is not empty, we need to check if the element is
        # greater than the last element in the queue, if it is, we can
        # always append the element


# @lc code=end
