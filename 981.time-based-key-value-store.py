#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#


# @lc code=start
class TimeMap:
    def __init__(self):
        self.hash = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hash:
            self.hash[key][0].append(timestamp)
            self.hash[key][1].append(value)
        else:
            self.hash[key] = [[timestamp], [value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        list = self.hash[key][0]
        l, r = 0, len(list) - 1
        while l <= r:
            mid = (l + r) // 2
            if list[mid] == timestamp:
                return self.hash[key][1][mid]
            elif list[mid] < timestamp:
                l = mid + 1
            else:
                r = mid - 1

        return self.hash[key][1][r] if r < timestamp and r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end
