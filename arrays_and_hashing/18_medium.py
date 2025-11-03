from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique quadruplets in the array that sum to the target value.
        
        Problem Understanding:
        - Given an array of integers and a target sum
        - Find all unique combinations of 4 numbers that add up to target
        - Each number can only be used once per quadruplet
        - Return results without duplicate quadruplets
        
        Approach:
        - Sort the array to enable two-pointer technique and duplicate skipping
        - Fix first two numbers using nested loops
        - Use two pointers for the remaining two numbers
        - Skip duplicates at each level to ensure uniqueness
        - Two-pointer search for the remaining sum after fixing first two
        
        Time Complexity: O(n³) where n is the length of the array
        Space Complexity: O(1) excluding the output array
        
        Args:
            nums: List of integers
            target: Target sum for quadruplets
            
        Returns:
            List of unique quadruplets that sum to target
        """
        # If array has fewer than 4 elements, no valid quadruplets possible
        if len(nums) < 4:
            return []
        
        # Sort array to enable two-pointer technique and duplicate detection
        nums.sort()
        result = []
        n = len(nums)
        
        # Fix first number (index i)
        for i in range(n - 3):  # Need at least 3 more elements after i
            # Skip duplicates for first number to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Fix second number (index j)
            for j in range(i + 1, n - 2):  # Need at least 2 more elements after j
                # Skip duplicates for second number to avoid duplicate quadruplets
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Two pointers for remaining two numbers
                left = j + 1    # Third pointer (after j)
                right = n - 1   # Fourth pointer (at end of array)
                
                # Two-pointer search for remaining sum
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        # Found valid quadruplet
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move both pointers and skip duplicates to find next unique combination
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif current_sum < target:
                        # Sum too small, move left pointer right to increase sum
                        left += 1
                    else:
                        # Sum too large, move right pointer left to decrease sum
                        right -= 1
        
        return result
    
def run_four_sum_test(nums, target, expected, test_name):
    """
    Tests the fourSum function with sorted comparison.
    
    Args:
        nums: Input list of integers
        target: Target sum for quadruplets
        expected: Expected list of quadruplets
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.fourSum(nums, target)
    # Sort both result and expected for consistent comparison
    result.sort()
    expected.sort()
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_four_sum_test([1,0,-1,0,-2,2], 0, [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]], "Example 1: Basic case")
run_four_sum_test([2,2,2,2,2], 8, [[2,2,2,2]], "Example 2: All same values")
run_four_sum_test([1,2,3,4], 10, [[1,2,3,4]], "Edge case: Single valid combination")
run_four_sum_test([1,2,3,4], 15, [], "Edge case: No valid combinations")
run_four_sum_test([1,2,3,4,5,6], 10, [[1,2,3,4]], "Edge case: Multiple numbers, single result")
run_four_sum_test([-1,-5,-5,-3,2,5,0,4], -7, [[-5,-5,2,4],[-5,-3,0,2]], "Edge case: Negative numbers")
run_four_sum_test([1,1,1,1], 4, [[1,1,1,1]], "Edge case: All same, exact match")
run_four_sum_test([], 0, [], "Edge case: Empty array")
run_four_sum_test([1,2,3], 6, [], "Edge case: Less than 4 elements")
run_four_sum_test([0,0,0,0], 0, [[0,0,0,0]], "Edge case: All zeros")
run_four_sum_test([1,2,3,4,5,6,7,8], 10, [[1,2,3,4]], "Edge case: Larger array")