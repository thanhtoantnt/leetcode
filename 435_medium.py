from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time (greedy approach)
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        prev_end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < prev_end:  # Overlapping
                count += 1
            else:  # Non-overlapping
                prev_end = end
        
        return count