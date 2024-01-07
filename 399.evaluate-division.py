#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#


# @lc code=start
import collections


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        hash = collections.defaultdict(list)
        for index, eq in enumerate(equations):
            up, down = eq
            hash[up].append((down, values[index]))
            hash[down].append((up, 1 / values[index]))

        def bfs(start, end):
            if start not in hash or end not in hash:
                return -1
            if start == end:
                return 1
            queue = [(start, 1)]  # (node, val)
            visited = set()
            while queue:
                node, val = queue.pop(0)
                if node == end:
                    return val
                visited.add(node)
                for nei, v in hash[node]:
                    if nei not in visited:
                        queue.append((nei, val * v))
            return -1

        return [bfs(up, down) for up, down in queries]


# @lc code=end
