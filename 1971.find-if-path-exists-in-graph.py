#
# @lc app=leetcode id=1971 lang=python3
#
# [1971] Find if Path Exists in Graph
#


# @lc code=start
class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True
        connected = dict()
        for edge in edges:
            if edge[0] not in connected:
                connected[edge[0]] = set()
            if edge[1] not in connected:
                connected[edge[1]] = set()
            connected[edge[0]].add(edge[1])
            connected[edge[1]].add(edge[0])

        queue = [source]
        visitedNode = set()
        while queue:
            node = queue.pop(0)
            if node not in visitedNode:
                if node == destination:
                    return True
                visitedNode.add(node)
                if node in connected:
                    queue.extend(connected[node] - visitedNode)
        return False


# @lc code=end
