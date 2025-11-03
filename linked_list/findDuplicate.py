from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect if there's a cycle using Floyd's algorithm
        slow = fast = nums[0]  # Start at index 0
        
        # Move slow one step, fast two steps until they meet
        while True:
            slow = nums[slow]           # Move slow pointer one step
            fast = nums[nums[fast]]     # Move fast pointer two steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle (duplicate number)
        # Reset one pointer to start, keep other at meeting point
        slow = nums[0]
        
        # Move both one step at a time until they meet
        while slow != fast:
            slow = nums[slow]   # Move from start
            fast = nums[fast]   # Move from meeting point
        
        # When they meet, it's at the cycle entrance (duplicate number)
        return slow

# Test cases
def run_test_case(nums, expected, test_name):
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