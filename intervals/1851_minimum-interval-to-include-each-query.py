from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """For each query q: length of the shortest interval containing q
        (−1 if none). Sort both; sweep intervals by start, retire by
        end, answer queries from a heap of (length, end).
        O((n+q) log(n+q)).
        """
        import heapq

        intervals.sort()
        out = {}
        heap: list[tuple[int, int]] = []
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            out[q] = heap[0][0] if heap else -1
        return [out[q] for q in queries]


if __name__ == "__main__":
    ivs = [[1, 4], [2, 4], [3, 6], [4, 4]]
    qs = [2, 3, 4, 5]
    assert Solution().minInterval(ivs, qs) == [3, 3, 1, 4]
    print("ok")
