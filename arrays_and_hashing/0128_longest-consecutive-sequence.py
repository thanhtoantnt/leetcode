from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive sequence of numbers in the array.
        
        Problem Understanding:
        - Given an unsorted array of integers
        - Find the length of the longest sequence of consecutive numbers
        - The sequence doesn't need to be contiguous in the original array
        - Example: [100, 4, 200, 1, 3, 2] has consecutive sequence [1,2,3,4] of length 4
        
        Approach:
        - Convert array to set for O(1) lookup
        - For each number, check if it's the start of a sequence (num-1 not in set)
        - If it's a start, count how long the consecutive sequence extends
        - Track the maximum length found
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(n) for the set storage
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest consecutive sequence
        """
        # Convert to set for O(1) average lookup time
        numSet = set(nums)
        
        # Track the maximum consecutive sequence length found
        largest = 0

        for num in numSet:
            # Only start counting if this is the beginning of a sequence
            # (i.e., num-1 is not in the set)
            if num - 1 not in numSet:
                # Start of a new consecutive sequence
                count = 1
                loopNum = num + 1  # Next number to check
                
                # Count how long the consecutive sequence extends
                while loopNum in numSet:
                    count += 1
                    loopNum += 1
                
                # Update maximum length if current sequence is longer
                largest = max(largest, count)

        return largest

def run_consecutive_test(nums, expected, test_name):
    """
    Tests the longestConsecutive function.
    
    Args:
        nums: Input list of integers
        expected: Expected length of longest consecutive sequence
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.longestConsecutive(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_consecutive_test([100,4,200,1,3,2], 4, "Example 1: [100,4,200,1,3,2] -> [1,2,3,4]")
run_consecutive_test([0,3,7,2,5,8,4,6,0,1], 9, "Example 2: [0,3,7,2,5,8,4,6,0,1] -> [0,1,2,3,4,5,6,7,8]")
run_consecutive_test([], 0, "Edge case: Empty array")
run_consecutive_test([1], 1, "Edge case: Single element")
run_consecutive_test([1,2,0,1], 3, "Edge case: Duplicates with consecutive numbers")
run_consecutive_test([1,2,3,4,5], 5, "Edge case: Already sorted consecutive")
run_consecutive_test([5,4,3,2,1], 5, "Edge case: Reverse sorted consecutive")
run_consecutive_test([1,3,5,7,9], 1, "Edge case: No consecutive numbers")
run_consecutive_test([1,1,1,1,1], 1, "Edge case: All same numbers")
run_consecutive_test([1,1,2,2,3,3,4,4], 4, "Edge case: Duplicates with consecutive")
run_consecutive_test([-3,-2,-1,0,1,2], 6, "Edge case: Negative numbers with consecutive")
run_consecutive_test([9,1,4,7,3,-1,0,5,8,-1,6], 9, "Edge case: Mixed numbers with many consecutive")