from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        if grid[0][0] != 0:
            return -1

        rows, cols = len(grid), len(grid[0])

        queue = deque()
        # step 1: add top-left cell
        queue.append((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        steps = 0
        while queue:
            level_size = len(queue)
            steps += 1
            for _ in range(level_size):
                i, j = queue.popleft()
                # print(f"i = {i}, j = {j}")
                if i == rows - 1 and j == cols - 1:
                    return steps

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < 0 or ni >= rows or nj < 0 or nj >= cols:
                        continue

                    if grid[ni][nj] == 0:
                        queue.append((ni, nj))
                        grid[ni][nj] = 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0,1],[1,0]]
    print(sol.shortestPathBinaryMatrix(grid1))  # Expected: 2

    grid2 = [[0,0,0],[1,1,0],[1,1,0]]
    print(sol.shortestPathBinaryMatrix(grid2))  # Expected: 4

    grid3 = [[1,0,0],[1,1,0],[1,1,0]]
    print(sol.shortestPathBinaryMatrix(grid3))  # Expected: -1
    
    grid4 = [[0]]  # Expected: 1
    print(sol.shortestPathBinaryMatrix(grid4))
    
    grid5 = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.shortestPathBinaryMatrix(grid5))  # Expected: 4