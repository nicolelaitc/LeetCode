#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random


class RandomizedSet:
    def __init__(self):
        self.list = []

    def insert(self, val: int) -> bool:
        l, r = 0, len(self.list)
        while l < r:
            mid = (l + r) // 2
            if self.list[mid] == val:
                return False
            elif self.list[mid] > val:
                r = mid
            else:
                l = mid + 1
        self.list.insert(l, val)
        return True

    def remove(self, val: int) -> bool:
        l, r = 0, len(self.list)
        while l < r:
            mid = (l + r) // 2
            if self.list[mid] == val:
                self.list.pop(mid)
                return True
            elif self.list[mid] > val:
                r = mid
            else:
                l = mid + 1
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
