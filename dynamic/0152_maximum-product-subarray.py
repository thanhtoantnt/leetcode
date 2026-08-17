from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Finds the maximum product of any contiguous subarray.
        
        Problem Understanding:
        - Given an integer array, find the subarray with the largest product
        - Return the maximum product value
        - Subarray is a contiguous sequence of elements
        
        Approach:
        - Use dynamic programming, keeping track of both maximum and minimum products ending at each position
        - This is necessary because a negative number can turn a small (negative) product into a large positive product
        - At each position, the maximum product could be:
          1. Current element itself (starting new subarray)
          2. Current element * previous maximum product
          3. Current element * previous minimum product (if both are negative)
        - Keep track of global maximum throughout the process
        
        Time Complexity: O(n) where n is length of nums
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum product of any contiguous subarray
        """
        if not nums:
            return 0
        
        # Initialize with first element
        max_product = nums[0]  # Global maximum product
        current_max = nums[0]  # Maximum product ending at current position
        current_min = nums[0]  # Minimum product ending at current position
        
        # Process remaining elements
        for i in range(1, len(nums)):
            # If current number is negative, swapping max and min will give correct results
            # because multiplying by negative flips the sign
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            
            # Calculate new max and min products ending at current position
            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])
            
            # Update global maximum
            max_product = max(max_product, current_max)
        
        return max_product

def run_max_product_test(nums, expected, test_name):
    """
    Tests the maxProduct function.
    
    Args:
        nums: List of integers
        expected: Expected maximum product
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.maxProduct(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_max_product_test([2,3,-2,4], 6, "Example 1: [2,3,-2,4] -> 6 (subarray [2,3])")
run_max_product_test([-2,0,-1], 0, "Example 2: [-2,0,-1] -> 0")
run_max_product_test([-2,3,-4], 24, "Edge case: [-2,3,-4] -> 24 (subarray [-2,3,-4])")
run_max_product_test([2,-5,-2,-4,3], 24, "Edge case: [2,-5,-2,-4,3] -> 24")
run_max_product_test([1], 1, "Edge case: Single element [1] -> 1")
run_max_product_test([-1], -1, "Edge case: Single negative [-1] -> -1")
run_max_product_test([0,2], 2, "Edge case: [0,2] -> 2")
run_max_product_test([-1,-2,-3], 6, "Edge case: All negative [-1,-2,-3] -> 6 (subarray [-2,-3])")
run_max_product_test([1,-2,3,-4,-5], 24, "Edge case: [1,-2,3,-4,-5] -> 24")
run_max_product_test([-3,-1,-1], 3, "Edge case: [-3,-1,-1] -> 3")
run_max_product_test([0,-1,2,-3,-4], 24, "Edge case: [0,-1,2,-3,-4] -> 24")
run_max_product_test([2,-2,3,4,-5], 24, "Edge case: [2,-2,3,4,-5] -> 24 (subarray [2,-2,3,4])")