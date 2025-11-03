from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to target.
        
        Problem Understanding:
        - Given an array of distinct integers and a target sum
        - Find all unique combinations that sum to target
        - Same number can be chosen multiple times
        - Each combination should be a unique set of numbers
        
        Approach:
        - Use backtracking to explore all possible combinations
        - At each step, try each candidate starting from current index (to avoid duplicates)
        - If adding a number doesn't exceed target, continue recursively
        - If sum equals target, add combination to result
        - Backtrack by removing the last added number
        
        Time Complexity: O(N^(T/M)) where N is number of candidates, T is target, M is minimal candidate
        Space Complexity: O(T/M) for recursion depth
        
        Args:
            candidates: List of distinct integers
            target: Target sum to achieve
            
        Returns:
            List of all unique combinations that sum to target
        """
        result = []
        
        def backtrack(start, current_combination, remaining_target):
            # Base case: if remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(current_combination[:])  # Add a copy of current combination
                return
            
            # If remaining target is negative, this path is invalid
            if remaining_target < 0:
                return
            
            # Try each candidate starting from 'start' index to avoid duplicates
            for i in range(start, len(candidates)):
                # Add current candidate to combination
                current_combination.append(candidates[i])
                
                # Recursively explore with the same index (i) since we can reuse the same number
                backtrack(i, current_combination, remaining_target - candidates[i])
                
                # Backtrack: remove the last added candidate
                current_combination.pop()
        
        backtrack(0, [], target)
        return result

def run_combination_sum_test(candidates, target, expected, test_name):
    """
    Tests the combinationSum function.
    
    Args:
        candidates: List of distinct integers
        target: Target sum to achieve
        expected: Expected list of combinations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.combinationSum(candidates, target)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(sorted(combo)) for combo in result)
    expected_set = set(tuple(sorted(combo)) for combo in expected)
    
    print(f"{test_name}:")
    print(f"  Input: candidates = {candidates}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_combination_sum_test([2,3,6,7], 7, [[2,2,3],[7]], "Example 1: [2,3,6,7], target=7 -> [[2,2,3],[7]]")
run_combination_sum_test([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]], "Example 2: [2,3,5], target=8 -> [[2,2,2,2],[2,3,3],[3,5]]")
run_combination_sum_test([2], 1, [], "Example 3: [2], target=1 -> []")
run_combination_sum_test([1], 1, [[1]], "Edge case: [1], target=1 -> [[1]]")
run_combination_sum_test([1], 2, [[1,1]], "Edge case: [1], target=2 -> [[1,1]]")
run_combination_sum_test([1,2], 4, [[1,1,1,1],[1,1,2],[2,2]], "Edge case: [1,2], target=4 -> [[1,1,1,1],[1,1,2],[2,2]]")
run_combination_sum_test([2,3,4], 6, [[2,2,2],[3,3],[2,4]], "Edge case: [2,3,4], target=6 -> [[2,2,2],[3,3],[2,4]]")
run_combination_sum_test([7,3,2], 18, [[2,2,2,2,2,2,2,2,2],[2,2,2,2,2,2,3,3],[2,2,2,3,7],[2,2,7,7],[2,3,3,3,3,3],[2,3,3,7,3],[3,3,3,3,3,3],[3,3,3,7,2],[3,7,7,1],[7,7,2,2]], "Edge case: [7,3,2], target=18 -> complex combinations")
run_combination_sum_test([], 1, [], "Edge case: Empty candidates -> []")
run_combination_sum_test([1,2,3], 0, [[]], "Edge case: Target 0 -> [[]]")