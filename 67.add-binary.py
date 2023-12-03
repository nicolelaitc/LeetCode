#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = -1, -1
        result = "0"
        while i >= -len(a) or j >= -len(b):
            first = a[i] if i >= -len(a) else "0"
            second = b[j] if j >= -len(b) else "0"
            count = sum([var == "1" for var in [first, second, result[0]]])
            # check i and j and latest result
            if count == 3:
                result = "11" + result[1:]
            elif count == 2:
                result = "10" + result[1:]
            elif count == 1:
                result = "01" + result[1:]
            else:
                result = "00" + result[1:]

            print(first, second, result)
            i -= 1
            j -= 1

        # remove zero \
        while True:
            if result[0] == "0" and len(result) > 1:
                result = result[1:]
            else:
                break
        return result


# @lc code=end
