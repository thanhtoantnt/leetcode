from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals in the given list.
        
        Problem Understanding:
        - Given an array of intervals where intervals[i] = [start_i, end_i]
        - Merge all overlapping intervals
        - Return an array of the non-overlapping intervals that cover all the intervals in the input
        
        Approach:
        - Sort intervals by start time to process them in chronological order
        - Initialize result with first interval
        - For each subsequent interval, check if it overlaps with the last merged interval
        - If overlapping, merge by extending the end time to max of both ends
        - If not overlapping, add as new interval to result
        
        Time Complexity: O(n log n) where n is the number of intervals (sorting dominates)
        Space Complexity: O(1) extra space excluding the output array
        
        Args:
            intervals: List of intervals [start, end]
            
        Returns:
            List of merged non-overlapping intervals
        """
        # Handle empty input
        if not intervals:
            return []
        
        # Sort intervals by start time to process in chronological order
        # If start times are same, order doesn't matter for merging logic
        intervals.sort(key=lambda x: x[0])
        
        # Initialize result with first interval
        result = [intervals[0]]
        
        # Process remaining intervals
        for current_start, current_end in intervals[1:]:
            # Get the last interval in result (the one we might merge with)
            last_start, last_end = result[-1]
            
            # Check if current interval overlaps with last merged interval
            # Two intervals overlap if current_start <= last_end
            if current_start <= last_end:
                # Overlapping: merge by extending end time to max of both ends
                # Keep the same start time, update end time to maximum
                result[-1][1] = max(last_end, current_end)
            else:
                # Non-overlapping: add current interval as new entry
                result.append([current_start, current_end])
        
        return result

def run_merge_test(intervals, expected, test_name):
    """
    Tests the merge function.
    
    Args:
        intervals: Input list of intervals
        expected: Expected merged intervals
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.merge(intervals)
    
    print(f"{test_name}:")
    print(f"  Input: {intervals}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_merge_test([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]], "Example 1: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]")
run_merge_test([[1,4],[4,5]], [[1,5]], "Example 2: [[1,4],[4,5]] -> [[1,5]] (touching intervals)")
run_merge_test([[1,4],[0,4]], [[0,4]], "Edge case: [[1,4],[0,4]] -> [[0,4]] (overlapping, different order)")
run_merge_test([[1,4],[2,3]], [[1,4]], "Edge case: [[1,4],[2,3]] -> [[1,4]] (one interval contained in another)")
run_merge_test([[1,4],[0,0]], [[0,0],[1,4]], "Edge case: [[1,4],[0,0]] -> [[0,0],[1,4]] (no overlap)")
run_merge_test([[1,4],[0,2],[3,5]], [[0,5]], "Edge case: [[1,4],[0,2],[3,5]] -> [[0,5]] (multiple overlapping)")
run_merge_test([[1,4],[2,5],[3,6]], [[1,6]], "Edge case: [[1,4],[2,5],[3,6]] -> [[1,6]] (all overlapping)")
run_merge_test([[1,4]], [[1,4]], "Edge case: Single interval")
run_merge_test([], [], "Edge case: Empty input")
run_merge_test([[1,4],[5,6],[7,8]], [[1,4],[5,6],[7,8]], "Edge case: No overlapping intervals")
run_merge_test([[2,3],[4,5],[6,7],[8,9],[1,10]], [[1,10]], "Edge case: One interval contains all others")
run_merge_test([[2,3],[5,5],[2,2],[3,4],[3,4]], [[2,4],[5,5]], "Edge case: Multiple duplicates and overlaps")