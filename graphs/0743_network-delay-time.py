from typing import List
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Time for a signal to reach every node (weighted shortest paths
        from k). Dijkstra with a min-heap: O(E log V).

        Pop the closest unfinalized node; relax its edges; a node is
        finalized the moment it's popped (nonnegative weights make the
        pop order its true distance).
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {}
        heap = [(0, k)]
        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue
            dist[u] = d
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))
        return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    assert Solution().networkDelayTime(times, 4, 2) == 2
    print("ok")
