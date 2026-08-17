from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Returns all possible subsets (the power set) of the given array.
        
        Problem Understanding:
        - Given an integer array nums of unique elements
        - Return all possible subsets (combinations of elements)
        - The solution set must not contain duplicate subsets
        - Return the solution in any order
        
        Approach:
        - Use backtracking/recursion to build subsets incrementally
        - At each step, we have two choices: include or exclude current element
        - Build subsets by adding one element at a time and exploring both options
        - Alternative approach: iterative building where we add each element to all existing subsets
        
        Time Complexity: O(2^n * n) where n is the length of nums
        Space Complexity: O(2^n * n) for the result (2^n subsets, average size n/2)
        
        Args:
            nums: List of unique integers
            
        Returns:
            List of all possible subsets
        """
        result = []
        
        def backtrack(start, current_subset):
            # Add current subset to result (make a copy)
            result.append(current_subset[:])
            
            # Explore further elements to add to subset
            for i in range(start, len(nums)):
                # Include nums[i] in current subset
                current_subset.append(nums[i])
                
                # Recursively generate subsets starting from next element
                backtrack(i + 1, current_subset)
                
                # Backtrack: remove nums[i] to try other possibilities
                current_subset.pop()
        
        backtrack(0, [])
        return result

def run_subsets_test(nums, expected, test_name):
    """
    Tests the subsets function.
    
    Args:
        nums: Input list of unique integers
        expected: Expected list of all subsets
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.subsets(nums)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(sorted(subset)) for subset in result)
    expected_set = set(tuple(sorted(subset)) for subset in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_subsets_test([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]], "Example 1: [1,2,3] -> all 8 subsets")
run_subsets_test([0], [[],[0]], "Example 2: [0] -> 2 subsets")
run_subsets_test([1,2], [[],[1],[2],[1,2]], "Edge case: [1,2] -> 4 subsets")
run_subsets_test([1,2,3,4], [[],[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1,2,3],[1,2,4],[1,3,4],[2,3,4],[1,2,3,4]], "Edge case: [1,2,3,4] -> 16 subsets")
run_subsets_test([], [[]], "Edge case: Empty array -> [[]]")
run_subsets_test([5], [[],[5]], "Edge case: Single element [5] -> 2 subsets")
run_subsets_test([-1,1], [[],[-1],[1],[-1,1]], "Edge case: Negative numbers [-1,1] -> 4 subsets")
run_subsets_test([1,2,3,5], [[],[1],[2],[3],[5],[1,2],[1,3],[1,5],[2,3],[2,5],[3,5],[1,2,3],[1,2,5],[1,3,5],[2,3,5],[1,2,3,5]], "Edge case: [1,2,3,5] -> 16 subsets")
run_subsets_test([1,2,3,4,5], [], "Edge case: [1,2,3,4,5] -> 32 subsets")
run_subsets_test([100], [[],[100]], "Edge case: Large number [100] -> 2 subsets")