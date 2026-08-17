from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """Perimeter of the single island: count 4 per land cell minus
        2 for every adjacent land pair (each shared edge hides one side
        from each cell). O(m·n).
        """
        peri = 0
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    peri += 4
                    if r > 0 and grid[r - 1][c]:
                        peri -= 2
                    if c > 0 and grid[r][c - 1]:
                        peri -= 2
        return peri


if __name__ == "__main__":
    g = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    assert Solution().islandPerimeter(g) == 16
    print("ok")
