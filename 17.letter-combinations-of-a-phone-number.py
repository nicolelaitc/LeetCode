#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#


# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        ans: list[str] = []
        for i in range(0, len(digits)):
            if len(ans) == 0:
                ans += list(phone[digits[i]])
            else:
                while len(ans[0]) <= i:
                    n = ans.pop(0)
                    for l in phone[digits[i]]:
                        ans.append(n + l)
        return ans


# @lc code=end
