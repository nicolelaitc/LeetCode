#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
from collections import Counter


class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n

            def get_parent(self):
                return self.parent

            def find(self, p):
                # path compression
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                root_p, root_q = self.find(p), self.find(q)
                if root_p == root_q:
                    return 1

                # weighted quick-union
                if self.size[root_p] < self.size[root_q]:
                    self.parent[root_p] = root_q
                    self.size[root_q] += self.size[root_p]
                else:
                    self.parent[root_q] = root_p
                    self.size[root_p] += self.size[root_q]

                return 0

        def all_connected(comp: int, connections):
            uf = UnionFind(comp)
            emptyWire = 0
            for u, v in connections:
                emptyWire += uf.union(u, v)

            root = uf.find(0)
            parent_set = {root}
            for n in range(comp):
                tmp = uf.find(n)
                if tmp != root:
                    parent_set.add(tmp)
            wire_needed = len(parent_set) - 1
            print(wire_needed, emptyWire)
            if emptyWire >= wire_needed:
                return wire_needed
            else:
                return -1

        return all_connected(n, connections)

        # @lc code=end
