#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        Rows = [[root]] if root else []
        VisitedRows = []

        while Rows:
            CurrentRow = Rows.pop(0)
            VisitedRows.append([node.val for node in CurrentRow])
            NextRow = []
            while CurrentRow:
                CurrentNode = CurrentRow.pop(0)
                if CurrentNode:
                    if CurrentNode.left:
                        NextRow.append(CurrentNode.left)
                    if CurrentNode.right:
                        NextRow.append(CurrentNode.right)
            if NextRow != []:
                Rows.append(NextRow)

        return [max(row) for row in VisitedRows]


# @lc code=end
