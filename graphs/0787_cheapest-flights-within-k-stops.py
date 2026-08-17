from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """Cheapest flight with AT MOST k stops — Bellman-Ford, k+1 rounds.

        Each round relaxes every edge once using the PREVIOUS round's
        distances (a temp copy): after round r, dist[v] is the cheapest
        price using at most r edges. Capping rounds caps the stops.
        O(k·E).
        """
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp = dist[:]
            for u, v, w in flights:
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
            dist = tmp
        return dist[dst] if dist[dst] != float("inf") else -1


if __name__ == "__main__":
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    assert Solution().findCheapestPrice(3, flights, 0, 2, 1) == 200
    assert Solution().findCheapestPrice(3, flights, 0, 2, 0) == 500
    print("ok")
