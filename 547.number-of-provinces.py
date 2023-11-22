#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#


# @lc code=start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()

        def checkLink(i):
            if i not in visited:
                visited.add(i)
                for j in range(len(isConnected[i])):
                    if isConnected[i][j] == 1:
                        # create the recursion
                        checkLink(j)

        for node in isConnected:
            for i in range(len(node)):
                if i not in visited:
                    # it is not linked to the node you visited before
                    province += 1
                    checkLink(i)

        return province


# @lc code=end
