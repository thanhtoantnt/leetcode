from typing import List
import heapq


class Solution:
    def swimWater(self, grid: List[List[int]]) -> int:
        """Min time to swim diagonally corner-to-corner, where time =
        max elevation on the path. Modified Dijkstra on (maxEdge, cell):
        O(n² log n).
        """
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        best = {(0, 0): grid[0][0]}
        while heap:
            t, r, c = heapq.heappop(heap)
            if (r, c) == (n - 1, n - 1):
                return t
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    nt = max(t, grid[nr][nc])
                    if nt < best.get((nr, nc), float("inf")):
                        best[(nr, nc)] = nt
                        heapq.heappush(heap, (nt, nr, nc))
        return -1


if __name__ == "__main__":
    grid = [[0, 2], [1, 3]]
    assert Solution().swimWater(grid) == 3
    print("ok")
