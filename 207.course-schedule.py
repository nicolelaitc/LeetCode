#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect edge?
        if not prerequisites:
            return True
        courses = collections.defaultdict(list)

        for course, pre in prerequisites:
            courses[course].append(pre)

        visited = set()
        for n in range(numCourses):
            if not self.dfs(courses, n, visited):
                return False
        return True

    def dfs(self, courses, course, visited):
        if course in visited:
            return False
        visited.add(course)
        for pre in courses[course]:
            if not self.dfs(courses, pre, visited):
                return False
        visited.remove(course)
        courses[course] = []
        return True

        #     stack = []
        #     if not courses[n]:
        #         visited.add(n)
        #         continue
        #     else:
        #         stack += courses[n]
        #         print(f"1. n={n}, stack={stack}")
        #         while stack:
        #             pre = stack.pop(0)
        #             print(f"2. pre={pre}, stack={stack}")
        #             if pre not in visited:
        #                 courses[pre] = [x for x in courses[pre] if x not in visited]
        #                 if courses[pre]:
        #                     if pre == n:
        #                         return False
        #                     stack += courses[pre]
        #                 else:
        #                     visited.add(pre)
        #             print(f"courses={courses}")
        #     if set(courses[n]).issubset(visited):
        #         print(f"visited={visited}")
        #         visited.add(n)
        # return len(visited) == numCourses


# @lc code=end
