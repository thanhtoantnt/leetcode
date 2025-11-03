from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Finds the maximum area of water that can be contained between two lines.
        
        Problem Understanding:
        - Given an array of heights representing vertical lines
        - Find two lines that together with x-axis form a container that holds most water
        - Area = width * min(height[left], height[right])
        
        Approach:
        - Use two-pointer technique starting from both ends
        - Move the pointer with smaller height inward
        - The intuition: moving the taller line inward can only decrease area
        - Moving the shorter line might increase area if we find a taller line
        - Continue until pointers meet
        
        Time Complexity: O(n) where n is the length of height array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            height: List of integers representing heights of vertical lines
            
        Returns:
            Maximum area of water that can be contained
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            # Moving the taller line inward can only decrease area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

def run_max_area_test(height, expected, test_name):
    """
    Tests the maxArea function.
    
    Args:
        height: List of heights representing vertical lines
        expected: Expected maximum area
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.maxArea(height)
    
    print(f"{test_name}:")
    print(f"  Input: {height}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_max_area_test([1,8,6,2,5,4,8,3,7], 49, "Example 1: [1,8,6,2,5,4,8,3,7] -> 49")
run_max_area_test([1,1], 1, "Example 2: [1,1] -> 1")
run_max_area_test([4,3,2,1,4], 16, "Edge case: [4,3,2,1,4] -> 16")
run_max_area_test([1,2,1], 2, "Edge case: [1,2,1] -> 2")
run_max_area_test([1,2,4,3], 4, "Edge case: [1,2,4,3] -> 4")
run_max_area_test([2,3,4,5,18,17,6], 17, "Edge case: [2,3,4,5,18,17,6] -> 17")
run_max_area_test([1,2,3,4,5], 6, "Edge case: Sequential increasing -> 6")
run_max_area_test([5,4,3,2,1], 6, "Edge case: Sequential decreasing -> 6")
run_max_area_test([1], 0, "Edge case: Single element -> 0")
run_max_area_test([], 0, "Edge case: Empty array -> 0")
run_max_area_test([10,9,8,7,6,5,4,3,2,1], 25, "Edge case: Decreasing array -> 25")
run_max_area_test([1,2,3,4,5,6,7,8,9,10], 25, "Edge case: Increasing array -> 25")