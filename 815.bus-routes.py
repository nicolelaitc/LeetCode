#
# @lc app=leetcode id=815 lang=python3
#
# [815] Bus Routes
#

# @lc code=start


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        # my source:https://www.youtube.com/watch?v=odmGyOJM5EY

        if source == target:
            return 0

        des = dict()

        # use id to make sure it is different routes
        for i, route in enumerate(routes):
            if target in route and source in route:
                return 1
            for stop in route:
                if stop not in des:
                    des[stop] = set()
                des[stop].add(i)

        seen_stop = set()
        seen_route = set()
        queue = [source]
        ans = 0
        while queue:
            # this line is to ensure that all the stop in the same layer in the graph will be count only += 1 in ans
            for _ in range(len(queue)):
                s = queue.pop(0)
                if s == target:
                    return ans
                for r in des[s]:
                    # how to separate route and stop
                    if r not in seen_route:
                        seen_route.add(r)
                        for stop in routes[r]:
                            if stop not in seen_stop:
                                seen_stop.add(stop)
                                queue.append(stop)
            ans += 1

        return -1


# @lc code=end
