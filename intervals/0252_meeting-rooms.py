from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """No two meetings overlap (touching endpoints is fine)?

        Sort by start; any meeting starting before the previous ends
        → conflict. O(n log n).
        """
        intervals.sort()
        return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))


if __name__ == "__main__":
    assert Solution().canAttendMeetings([[0, 30], [5, 10], [15, 20]]) is False
    assert Solution().canAttendMeetings([[7, 10], [2, 3]])
    print("ok")
