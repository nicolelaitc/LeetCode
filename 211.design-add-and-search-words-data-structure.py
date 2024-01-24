#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#


# @lc code=start
class WordDictionary:
    def __init__(self):
        # need to create data structure that are double linked?
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(root, word):
            if not word:
                return root.isEnd
            if root.children == {}:
                return False
            if word[0] in root.children:
                if len(word) == 1:
                    return root.children[word[0]].isEnd
                else:
                    return dfs(root.children[word[0]], word[1:])
            elif word[0] == ".":
                for child in root.children:
                    if dfs(root.children[child], word[1:]):
                        return True
                return False
            else:
                return False

        return dfs(self.node, word)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
