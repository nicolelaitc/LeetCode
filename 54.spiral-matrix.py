#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#


# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j = 0, 0
        visited = [[i, j]]
        ans = [matrix[i][j]]
        # the loop runs right, down, left, up
        # if it reached the end, go another direction
        # seq = ["right", "down", "left", "up"]
        direction = "right"
        counter = 1

        while True:
            if direction == "right":
                if j + 1 < len(matrix[0]) and [i, j + 1] not in visited:
                    j += 1
                    visited.append([i, j])
                    ans.append(matrix[i][j])
                    counter = 0
                else:
                    direction = "down"
                    counter += 1
            elif direction == "down":
                if i + 1 < len(matrix) and [i + 1, j] not in visited:
                    i += 1
                    visited.append([i, j])
                    ans.append(matrix[i][j])
                    counter = 0
                else:
                    direction = "left"
                    counter += 1
            elif direction == "left":
                if j - 1 >= 0 and [i, j - 1] not in visited:
                    j -= 1
                    visited.append([i, j])
                    ans.append(matrix[i][j])
                    counter = 0
                else:
                    direction = "up"
                    counter += 1
            elif direction == "up":
                if i - 1 >= 0 and [i - 1, j] not in visited:
                    i -= 1
                    visited.append([i, j])
                    ans.append(matrix[i][j])
                    counter = 0
                else:
                    direction = "right"
                    counter += 1

            if counter >= 4:
                return ans

            print(f"i: {i}, j: {j}, visited: {visited}, ans: {ans}")


# @lc code=end
