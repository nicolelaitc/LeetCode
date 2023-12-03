#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#


# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # i, j = -1, -1
        # result = "0"

        # while i >= -len(a) or j >= -len(b):
        #     first = a[i] if i >= -len(a) else "0"
        #     second = b[j] if j >= -len(b) else "0"
        #     count = sum([var == "1" for var in [first, second, result[0]]])
        #     # check i and j and latest result
        #     if count == 3:
        #         result = "11" + result[1:]
        #     elif count == 2:
        #         result = "10" + result[1:]
        #     elif count == 1:
        #         result = "01" + result[1:]
        #     else:
        #         result = "00" + result[1:]

        #     print(first, second, result)
        #     i -= 1
        #     j -= 1

        # # remove zero \
        # while True:
        #     if result[0] == "0" and len(result) > 1:
        #         result = result[1:]
        #     else:
        #         break
        # return result

        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0 or carry:
            carry += int(a[i]) if i >= 0 else 0
            carry += int(b[j]) if j >= 0 else 0
            result = str(carry % 2) + result
            carry //= 2
            i -= 1
            j -= 1
        return result


# @lc code=end
