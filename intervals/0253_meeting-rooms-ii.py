from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Minimum rooms to host all meetings = max simultaneous overlap.

        Sweep line: +1 at each start, −1 at each end, sort events
        (ends first on ties — a meeting ending at t frees the room for
        one starting at t). Peak concurrent count is the answer.
        O(n log n).
        """
        starts = sorted(s for s, _ in intervals)
        ends = sorted(e for _, e in intervals)
        rooms = best = 0
        i = j = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                best = max(best, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return best


if __name__ == "__main__":
    assert Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert Solution().minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert Solution().minMeetingRooms([[1, 5], [5, 10]]) == 1
    print("ok")
