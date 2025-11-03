from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray with the largest sum and returns that sum.
        
        Problem Understanding:
        - Given an integer array
        - Find the contiguous subarray (containing at least one number) which has the largest sum
        - Return the maximum sum possible
        
        Approach:
        - Use Kadane's Algorithm (Dynamic Programming)
        - At each position, decide whether to extend the existing subarray or start a new one
        - Keep track of current subarray sum and maximum sum seen so far
        - If current sum becomes negative, start fresh from next element
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: List of integers (can contain both positive and negative numbers)
            
        Returns:
            Maximum sum of any contiguous subarray
        """
        # Initialize with first element
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Process remaining elements
        for i in range(1, len(nums)):
            # At each position, decide whether to add to current subarray or start fresh
            # If current_sum is negative, starting fresh is better
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update maximum sum if current subarray sum is larger
            max_sum = max(max_sum, current_sum)
        
        return max_sum

def run_max_subarray_test(nums, expected, test_name):
    """
    Tests the maxSubArray function.
    
    Args:
        nums: Input list of integers
        expected: Expected maximum subarray sum
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.maxSubArray(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_max_subarray_test([-2,1,-3,4,-1,2,1,-5,4], 6, "Example 1: [-2,1,-3,4,-1,2,1,-5,4] -> 6 ([4,-1,2,1])")
run_max_subarray_test([1], 1, "Example 2: [1] -> 1")
run_max_subarray_test([5,4,-1,7,8], 23, "Example 3: [5,4,-1,7,8] -> 23 (entire array)")
run_max_subarray_test([-1], -1, "Edge case: Single negative")
run_max_subarray_test([-2,-1], -1, "Edge case: All negative, [-2,-1] -> -1")
run_max_subarray_test([1,2,3,4,5], 15, "Edge case: All positive -> sum of all")
run_max_subarray_test([-5,-2,-8,-1], -1, "Edge case: All negative -> least negative")
run_max_subarray_test([0], 0, "Edge case: Single zero")
run_max_subarray_test([1,-1,1,-1,1], 1, "Edge case: Alternating pattern")
run_max_subarray_test([-1,-2,-3,-4], -1, "Edge case: Decreasing negatives")
run_max_subarray_test([1,2,-1,-2,2,1,-2,1], 3, "Edge case: [2,1] or [1,-2,1,1] -> 3")
run_max_subarray_test([8,-19,5,-4,20], 21, "Edge case: [5,-4,20] -> 21")