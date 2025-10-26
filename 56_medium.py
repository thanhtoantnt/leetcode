from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        current_start, current_end = intervals[0]
        
        for start, end in intervals[1:]:
            if start <= current_end:  # Overlapping
                current_end = max(current_end, end)
            else:  # Non-overlapping
                merged.append([current_start, current_end])
                current_start, current_end = start, end
        
        # Add the last interval
        merged.append([current_start, current_end])
        
        return merged

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(sol.merge(intervals))