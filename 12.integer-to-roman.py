#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#


# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        res, count = "", 1
        while num > 0:
            remainder = num % 10
            if remainder < 4:
                res = roman[count] * remainder + res
            elif remainder == 4:
                res = roman[count] + roman[count * 5] + res
            elif remainder == 5:
                res = roman[count * 5] + res
            elif remainder < 9:
                res = roman[count * 5] + roman[count] * (remainder - 5) + res
            elif remainder == 9:
                res = roman[count] + roman[count * 10] + res

            count *= 10
            num //= 10
        return res


# @lc code=end
