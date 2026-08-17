from typing import List
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """Minimum spanning tree of points with Manhattan distance (Prim).

        Visit-based Prim: keep a min-heap of edge costs to the frontier;
        pop the cheapest, add its endpoint to the tree if unvisited,
        push all edges from the new vertex. O(n² log n) worst case.
        """
        n = len(points)
        visited = [False] * n
        heap = [(0, 0)]  # (cost, vertex)
        total = 0
        while heap:
            cost, u = heapq.heappop(heap)
            if visited[u]:
                continue
            visited[u] = True
            total += cost
            for v in range(n):
                if not visited[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (d, v))
        return total


if __name__ == "__main__":
    assert Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18  # 12 + 6
    assert Solution().minCostConnectPoints([[0, 0]]) == 0
    print("ok")
