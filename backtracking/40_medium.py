from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the candidate numbers sum to target.
        Each number in candidates may only be used once in the combination.
        
        Problem Understanding:
        - Given a collection of candidate numbers and a target sum
        - Find all unique combinations that sum to target
        - Each number can only be used once per combination
        - The solution set must not contain duplicate combinations
        
        Approach:
        - Use backtracking with sorted array to handle duplicates
        - Skip duplicate elements at the same recursion level to avoid duplicate combinations
        - At each step, try each candidate starting from current index
        - If adding a number doesn't exceed target, continue recursively
        - Backtrack by removing the last added number
        
        Time Complexity: O(2^N) in worst case where N is the length of candidates
        Space Complexity: O(target/min_candidate) for recursion depth
        
        Args:
            candidates: List of integers (may contain duplicates)
            target: Target sum to achieve
            
        Returns:
            List of all unique combinations that sum to target
        """
        # Sort the candidates to handle duplicates properly
        candidates.sort()
        result = []
        
        def backtrack(start, current_combination, remaining_target):
            # Base case: if remaining target is 0, we found a valid combination
            if remaining_target == 0:
                result.append(current_combination[:])  # Add a copy of current combination
                return
            
            # If remaining target is negative, this path is invalid
            if remaining_target < 0:
                return
            
            # Try each candidate starting from 'start' index
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                # If current element is same as previous and previous was not used (i > start),
                # then we've already considered this combination
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Add current candidate to combination
                current_combination.append(candidates[i])
                
                # Recursively explore with next index (i+1) since each number can only be used once
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                
                # Backtrack: remove the last added candidate
                current_combination.pop()
        
        backtrack(0, [], target)
        return result

def run_combination_sum2_test(candidates, target, expected, test_name):
    """
    Tests the combinationSum2 function.
    
    Args:
        candidates: List of integers (may contain duplicates)
        target: Target sum to achieve
        expected: Expected list of combinations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.combinationSum2(candidates, target)
    
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
run_combination_sum2_test([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]], "Example 1: [10,1,2,7,6,1,5], target=8 -> [[1,1,6],[1,2,5],[1,7],[2,6]]")
run_combination_sum2_test([2,5,2,1,2], 5, [[1,2,2],[5]], "Example 2: [2,5,2,1,2], target=5 -> [[1,2,2],[5]]")
run_combination_sum2_test([1], 1, [[1]], "Edge case: [1], target=1 -> [[1]]")
run_combination_sum2_test([1], 2, [], "Edge case: [1], target=2 -> []")
run_combination_sum2_test([1,1,1,1], 2, [[1,1]], "Edge case: [1,1,1,1], target=2 -> [[1,1]]")
run_combination_sum2_test([2,2,2,2], 2, [[2]], "Edge case: [2,2,2,2], target=2 -> [[2]]")
run_combination_sum2_test([1,2,3,4,5], 7, [[1,2,4],[2,5],[3,4]], "Edge case: [1,2,3,4,5], target=7 -> [[1,2,4],[2,5],[3,4]]")
run_combination_sum2_test([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 2, [[1,1]], "Edge case: Many duplicates")
run_combination_sum2_test([], 0, [[]], "Edge case: Empty array, target=0 -> [[]]")
run_combination_sum2_test([2,3,5], 1, [], "Edge case: [2,3,5], target=1 -> []")