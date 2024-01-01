#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = self.inorderTraversal(root)
        print(self.stack)

    def inorderTraversal(self, root):
        answer = []

        self.inorderTraversalUtil(root, answer)
        return answer

    def inorderTraversalUtil(self, root, answer):
        if root is None:
            return

        self.inorderTraversalUtil(root.left, answer)
        answer.append(root.val)
        self.inorderTraversalUtil(root.right, answer)
        return

    def next(self) -> int:
        if self.stack:
            return self.stack.pop(0)

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end
