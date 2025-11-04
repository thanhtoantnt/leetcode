from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a sorted array that add up to a target value.
        
        Problem Understanding:
        - Given a 1-indexed sorted array and target sum
        - Find two numbers that add up to target
        - Return their 1-indexed positions in an array [index1, index2]
        - Each input has exactly one solution, no element used twice
        - Must use constant extra space
        
        Approach:
        - Use two-pointer technique on the sorted array
        - Start with left pointer at beginning and right pointer at end
        - If sum equals target, return 1-indexed positions
        - If sum is less than target, move left pointer right (increase sum)
        - If sum is greater than target, move right pointer left (decrease sum)
        - Since array is sorted, this approach is guaranteed to find the solution
        
        Time Complexity: O(n) where n is the length of numbers array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            numbers: 1-indexed sorted array of integers
            target: Target sum to find
            
        Returns:
            List containing 1-indexed positions of two numbers that sum to target
        """
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                # Return 1-indexed positions
                return [left + 1, right + 1]
            elif current_sum < target:
                # Sum too small, move left pointer right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer left to decrease sum
                right -= 1
        
        # This should not be reached given the problem constraints
        return []

def run_two_sum_test(numbers, target, expected, test_name):
    """
    Tests the twoSum function.
    
    Args:
        numbers: Sorted array of integers
        target: Target sum to find
        expected: Expected 1-indexed positions
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.twoSum(numbers, target)
    
    print(f"{test_name}:")
    print(f"  Input: numbers = {numbers}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_two_sum_test([2,7,11,15], 9, [1,2], "Example 1: [2,7,11,15], target=9 -> [1,2] (2+7=9)")
run_two_sum_test([2,3,4], 6, [1,3], "Example 2: [2,3,4], target=6 -> [1,3] (2+4=6)")
run_two_sum_test([-1,0], -1, [1,2], "Example 3: [-1,0], target=-1 -> [1,2] (-1+0=-1)")
run_two_sum_test([1,2,3,4,5], 8, [3,5], "Edge case: [1,2,3,4,5], target=8 -> [3,5] (3+5=8)")
run_two_sum_test([1,2,3,4,5,6], 7, [1,6], "Edge case: [1,2,3,4,5,6], target=7 -> [1,6] (1+6=7)")
run_two_sum_test([1,2], 3, [1,2], "Edge case: [1,2], target=3 -> [1,2] (1+2=3)")
run_two_sum_test([1,2,3,4], 4, [1,3], "Edge case: [1,2,3,4], target=4 -> [1,3] (1+3=4)")
run_two_sum_test([1,2,3,4], 5, [1,4], "Edge case: [1,2,3,4], target=5 -> [1,4] (1+4=5)")
run_two_sum_test([1,2,3,4], 3, [1,2], "Edge case: [1,2,3,4], target=3 -> [1,2] (1+2=3)")
run_two_sum_test([5,25,75], 100, [2,3], "Edge case: [5,25,75], target=100 -> [2,3] (25+75=100)")
run_two_sum_test([1,1000000], 1000001, [1,2], "Edge case: Large numbers, target=1000001 -> [1,2]")
run_two_sum_test([1,2,3,4,5,6,7,8,9,10], 17, [7,10], "Edge case: [1,2,3,4,5,6,7,8,9,10], target=17 -> [7,10]")