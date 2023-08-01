#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

from collections import Counter


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if s == t:
            return s
        start, end = 0, 1
        min_window = ""
        hash_t = dict(Counter(t))
        hash_s = dict()
        hash_s_length = 0
        while end <= len(s):
            flag = False
            if hash_s_length < (end - start):
                hash_s_length += 1
                if s[start:end][-1] in hash_t:
                    if s[start:end][-1] in hash_s:
                        hash_s[s[start:end][-1]] += 1
                    else:
                        hash_s[s[start:end][-1]] = 1
            if end - start < len(t):
                end += 1
                continue
            # print("1", s[start:end], hash_s, hash_t, hash_s_length, min_window)
            if hash_s.keys() == hash_t.keys():
                for key in hash_t:
                    if hash_s[key] < hash_t[key]:
                        end += 1
                        flag = True
                        break
                if flag == False:
                    min_window = (
                        s[start:end]
                        if min_window == "" or (end - start) < len(min_window)
                        else min_window
                    )
                    if s[start:end][0] in hash_s:
                        hash_s[s[start:end][0]] -= 1
                    hash_s_length -= 1
                    start += 1
            else:
                end += 1
            # print("2", s[start:end], hash_s, hash_t, hash_s_length, min_window)

        return min_window


# @lc code=end
