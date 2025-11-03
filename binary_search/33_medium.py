from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.
        
        Problem Understanding:
        - Given a sorted array that may have been rotated at some pivot point
        - Find the index of target if it exists in the array, otherwise return -1
        - Must achieve O(log n) time complexity
        
        Approach:
        - Use modified binary search
        - At each step, determine which half of the array is sorted
        - Check if target lies within the sorted half
        - If yes, search in that half; if no, search in the other half
        - Continue until target is found or search space is exhausted
        
        Time Complexity: O(log n) where n is the length of nums array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: Rotated sorted array
            target: Value to search for
            
        Returns:
            Index of target if found, -1 otherwise
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                # Check if target lies in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                # Check if target lies in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1

def run_search_rotated_test(nums, target, expected, test_name):
    """
    Tests the search function for rotated sorted array.
    
    Args:
        nums: Rotated sorted array
        target: Value to search for
        expected: Expected index of target (-1 if not found)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.search(nums, target)
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_search_rotated_test([4,5,6,7,0,1,2], 0, 4, "Example 1: [4,5,6,7,0,1,2], target=0 -> 4")
run_search_rotated_test([4,5,6,7,0,1,2], 3, -1, "Example 2: [4,5,6,7,0,1,2], target=3 -> -1")
run_search_rotated_test([1], 0, -1, "Example 3: [1], target=0 -> -1")
run_search_rotated_test([1], 1, 0, "Edge case: Single element [1], target=1 -> 0")
run_search_rotated_test([1,3], 3, 1, "Edge case: Two elements [1,3], target=3 -> 1")
run_search_rotated_test([3,1], 1, 1, "Edge case: Two elements [3,1], target=1 -> 1")
run_search_rotated_test([1,2,3,4,5], 3, 2, "Edge case: No rotation [1,2,3,4,5], target=3 -> 2")
run_search_rotated_test([5,1,2,3,4], 1, 1, "Edge case: [5,1,2,3,4], target=1 -> 1")
run_search_rotated_test([2,3,4,5,1], 5, 3, "Edge case: [2,3,4,5,1], target=5 -> 3")
run_search_rotated_test([6,7,8,1,2,3,4,5], 3, 5, "Edge case: [6,7,8,1,2,3,4,5], target=3 -> 5")
run_search_rotated_test([4,5,6,7,8,1,2,3], 8, 4, "Edge case: [4,5,6,7,8,1,2,3], target=8 -> 4")
run_search_rotated_test([1,2,3,4,5,6,7,8], 4, 3, "Edge case: No rotation [1,2,3,4,5,6,7,8], target=4 -> 3")