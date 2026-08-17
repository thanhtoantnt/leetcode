from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Finds the duplicate number in an array using Floyd's Cycle Detection Algorithm.
        
        Problem Understanding:
        - Array contains n+1 integers where each integer is in range [1, n]
        - Exactly one number appears multiple times
        - Must not modify array and use only O(1) extra space
        - Find the duplicate number
        
        Approach:
        - Treat array as a linked list where nums[i] points to index nums[i]
        - The duplicate number creates a cycle in this "linked list"
        - Use Floyd's algorithm to detect cycle and find entrance
        - Phase 1: Detect cycle using slow/fast pointers
        - Phase 2: Find cycle entrance (the duplicate number)
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: Array of n+1 integers in range [1, n] with one duplicate
            
        Returns:
            The duplicate number
        """
        # Phase 1: Detect if there's a cycle using Floyd's algorithm
        # Start both pointers at index 0
        slow = fast = nums[0]  # Start at index 0
        
        # Move slow one step, fast two steps until they meet
        while True:
            slow = nums[slow]           # Move slow pointer one step (nums[slow])
            fast = nums[nums[fast]]     # Move fast pointer two steps (nums[nums[fast]])
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate number)
        # Reset one pointer to start (index 0), keep other at meeting point
        slow = nums[0]
        
        # Move both one step at a time until they meet
        while slow != fast:
            slow = nums[slow]   # Move from start (index 0)
            fast = nums[fast]   # Move from meeting point
        
        # When they meet, it's at the cycle entrance (duplicate number)
        return slow

# Test cases
def run_test_case(nums, expected, test_name):
    """
    Tests the findDuplicate function.
    
    Args:
        nums: Input array with one duplicate
        expected: Expected duplicate number
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findDuplicate(nums)
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run all test cases
run_test_case([1,3,4,2,2], 2, "Example 1: Basic case")
run_test_case([3,1,3,4,2], 3, "Example 2: Different duplicate")
run_test_case([3,3,3,3,3], 3, "Example 3: All same except one")
run_test_case([1,1], 1, "Edge case: Two elements, both same")
run_test_case([2,2,2,2,2], 2, "Edge case: All elements same")
run_test_case([1,4,4,2,4], 4, "Edge case: Multiple occurrences")
run_test_case([1,2,3,4,5,5], 5, "Edge case: Duplicate at end")
run_test_case([5,1,2,3,4,5], 5, "Edge case: Duplicate at beginning")
run_test_case([1,2,5,3,5,4], 5, "Edge case: Duplicate in middle")

# Additional verification for the algorithm's path
def trace_path(nums):
    """
    Traces the path of the algorithm to visualize the cycle detection.
    
    Args:
        nums: Array to trace path for
    """
    print(f"Tracing path for {nums}:")
    path = []
    visited = set()
    current = 0  # Start at index 0
    while current not in visited and current < len(nums):
        visited.add(current)
        path.append(f"index {current} -> value {nums[current]}")
        current = nums[current]
        if current >= len(nums):
            break
    path.append(f"index {current} (cycle start)")
    print("  " + " -> ".join(path))
    print()

print("Path tracing for verification:")
trace_path([1,3,4,2,2])
trace_path([3,1,3,4,2])