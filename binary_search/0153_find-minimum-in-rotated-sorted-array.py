from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.
        
        Problem Understanding:
        - Given a sorted array rotated between 1 and n times
        - All integers are unique
        - Need to find the minimum element in O(log n) time
        
        Approach:
        - Use binary search to find the rotation point
        - Compare middle element with rightmost element to determine which half contains the minimum
        - If nums[mid] > nums[right], minimum is in the right half
        - If nums[mid] <= nums[right], minimum is in the left half (including mid)
        - Continue until we find the minimum
        
        Time Complexity: O(log n) where n is the length of nums array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: Rotated sorted array
            
        Returns:
            Minimum element in the array
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than rightmost element,
            # the minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid element is less than or equal to rightmost element,
            # the minimum could be mid or in the left half
            else:
                right = mid
        
        # At this point, left == right, which is the minimum element
        return nums[left]

def run_find_min_test(nums, expected, test_name):
    """
    Tests the findMin function.
    
    Args:
        nums: Rotated sorted array
        expected: Expected minimum element
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findMin(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_find_min_test([3,4,5,1,2], 1, "Example 1: [3,4,5,1,2] -> 1")
run_find_min_test([4,5,6,7,0,1,2], 0, "Example 2: [4,5,6,7,0,1,2] -> 0")
run_find_min_test([11,13,15,17], 11, "Example 3: [11,13,15,17] -> 11 (no rotation)")
run_find_min_test([2,1], 1, "Edge case: Two elements [2,1] -> 1")
run_find_min_test([1,2], 1, "Edge case: Two elements [1,2] -> 1")
run_find_min_test([1], 1, "Edge case: Single element [1] -> 1")
run_find_min_test([2,3,4,5,1], 1, "Edge case: [2,3,4,5,1] -> 1")
run_find_min_test([5,1,2,3,4], 1, "Edge case: [5,1,2,3,4] -> 1")
run_find_min_test([1,2,3,4,5], 1, "Edge case: [1,2,3,4,5] -> 1 (no rotation)")
run_find_min_test([3,4,1,2], 1, "Edge case: [3,4,1,2] -> 1")
run_find_min_test([5,6,1,2,3,4], 1, "Edge case: [5,6,1,2,3,4] -> 1")
run_find_min_test([6,7,8,1,2,3,4,5], 1, "Edge case: [6,7,8,1,2,3,4,5] -> 1")