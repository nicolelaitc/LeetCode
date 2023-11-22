#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = [root]
        ans = [root.val]
        p = 0
        while p < len(queue):
            node = queue[p]
            if node != None:
                left = node.left if node.left else None
                queue.append(left)
                ans.append(left.val if left else "null")
                right = node.right if node.right else None
                queue.append(right)
                ans.append(right.val if right else "null")
            p += 1
        print(ans)
        while ans[-1] == "null":
            ans = ans[:-1]
        print(ans)
        ans_str = f"{','.join(map(str, ans))}"
        print(ans_str)
        return ans_str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        arr.pop(0)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node != None:
                left = arr.pop(0) if arr else None
                if left and left != "null":
                    node.left = TreeNode(int(left))
                    queue.append(node.left)
                right = arr.pop(0) if arr else None
                if right and right != "null":
                    node.right = TreeNode(int(right))
                    queue.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
