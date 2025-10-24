from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []

        rows = len(mat)
        cols = len(mat[0])

        results = [[-1] * cols for _ in range(rows)]

        # print(f"rows = {rows}, cols = {cols}")
        # Add all 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    results[i][j] = 0
                    # print(f"i = {i}, j = {j}")
                    queue.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # print(results)
        # BFS
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                i, j = queue.popleft()
                # print(f"i = {i}, j = {j}")

                for dx, dy in directions:
                    ni = i + dx
                    nj = j + dy

                    if ni < 0 or nj < 0 or ni >= rows or nj >= cols:
                        continue

                    if results[ni][nj] == -1:
                        results[ni][nj] = 1 + results[i][j]
                        queue.append((ni, nj))
        
        return results

if __name__ == "__main__":
    sol = Solution()

    mat1 = [[0,0,0],[0,1,0],[0,0,0]]
    print(sol.updateMatrix(mat1))  # Expected: [[0,0,0],[0,1,0],[0,0,0]]
    
    mat2 = [[0,0,0],[0,1,0],[1,1,1]]
    print(sol.updateMatrix(mat2))  # Expected: [[0,0,0],[0,1,0],[1,2,1]]
    
    mat3 = [[0]]
    print(sol.updateMatrix(mat3))  # Expected: [[0]]
    
    mat4 = [[1,1,1],[1,1,1],[1,1,0]]
    print(sol.updateMatrix(mat4))  # Expected: [[4,3,2],[3,2,1],[2,1,0]]
