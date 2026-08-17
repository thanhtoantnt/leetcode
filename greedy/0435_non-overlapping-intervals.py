from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        Finds the minimum number of intervals to remove to make the rest non-overlapping.
        
        Problem Understanding:
        - Given an array of intervals where intervals[i] = [start_i, end_i]
        - Return the minimum number of intervals that need to be removed
        - So that the remaining intervals do not overlap
        
        Approach:
        - Use greedy algorithm with sorting
        - Sort intervals by their end times to prioritize intervals that finish earlier
        - This maximizes the space left for other intervals
        - Iterate through sorted intervals and keep track of the end time of the last kept interval
        - If the current interval starts before the last kept interval ends, it overlaps and needs removal
        - Otherwise, update the last kept end time
        - Count the number of overlapping intervals that need removal
        
        Time Complexity: O(n log n) due to sorting, where n is the number of intervals
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            intervals: List of intervals [start, end]
            
        Returns:
            Minimum number of intervals to remove
        """
        if not intervals:
            return 0
        
        # Sort intervals by their end times (greedy choice)
        intervals.sort(key=lambda x: x[1])
        
        # Count of intervals to remove
        remove_count = 0
        
        # End time of the last kept interval
        last_end = intervals[0][1]
        
        # Process remaining intervals
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i][0], intervals[i][1]
            
            # If current interval starts before the last kept interval ends, it overlaps
            if current_start < last_end:
                # This interval needs to be removed
                remove_count += 1
            else:
                # No overlap, update the last kept end time
                last_end = current_end
        
        return remove_count

def run_erase_overlap_test(intervals, expected, test_name):
    """
    Tests the eraseOverlapIntervals function.
    
    Args:
        intervals: List of intervals [start, end]
        expected: Expected minimum number of intervals to remove
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.eraseOverlapIntervals(intervals)
    
    print(f"{test_name}:")
    print(f"  Input: {intervals}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_erase_overlap_test([[1,2],[2,3],[3,4],[1,3]], 1, "Example 1: [[1,2],[2,3],[3,4],[1,3]] -> 1 (remove [1,3])")
run_erase_overlap_test([[1,2],[1,2],[1,2]], 2, "Example 2: [[1,2],[1,2],[1,2]] -> 2 (remove 2 intervals)")
run_erase_overlap_test([[1,2],[2,3]], 0, "Example 3: [[1,2],[2,3]] -> 0 (no overlap)")
run_erase_overlap_test([[1,100],[11,22],[1,11],[2,12]], 2, "Edge case: [[1,100],[11,22],[1,11],[2,12]] -> 2")
run_erase_overlap_test([[1,4],[2,3],[3,5],[4,6]], 1, "Edge case: [[1,4],[2,3],[3,5],[4,6]] -> 1")
run_erase_overlap_test([], 0, "Edge case: Empty intervals -> 0")
run_erase_overlap_test([[1,2]], 0, "Edge case: Single interval -> 0")
run_erase_overlap_test([[1,4],[2,3],[3,4]], 1, "Edge case: [[1,4],[2,3],[3,4]] -> 1")
run_erase_overlap_test([[0,1],[1,2],[2,3],[3,4]], 0, "Edge case: Non-overlapping intervals -> 0")
run_erase_overlap_test([[1,3],[2,4],[3,5]], 1, "Edge case: [[1,3],[2,4],[3,5]] -> 1")
run_erase_overlap_test([[1,3],[2,4],[1,4]], 2, "Edge case: [[1,3],[2,4],[1,4]] -> 2")
run_erase_overlap_test([[-5,1],[1,2],[2,3],[3,4]], 0, "Edge case: With negative start -> 0")