"""
Combination Sum Solution with Explanations and Unit Tests

This file contains the solution for the Combination Sum problem
along with comprehensive explanations and unit tests.
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations where candidate numbers sum to target.
        Each number may be used unlimited times.
        
        Args:
            candidates (List[int]): List of distinct integers
            target (int): Target sum value
            
        Returns:
            List[List[int]]: All unique combinations that sum to target
        """
        # Sort candidates to enable ordered processing and early termination
        candidates.sort()
        # dp[i] will store all combinations that sum to i
        dp = [[] for _ in range(target + 1)]
        
        for num in range(target + 1):
            for candidate in candidates:
                if candidate > num:
                    break  # No need to check larger candidates
                elif candidate == num:
                    # Direct match: candidate itself forms a valid combination
                    dp[num].append([candidate])
                else:  # candidate < num
                    # Check all combinations that sum to (num - candidate)
                    for combination in dp[num - candidate]:
                        # Only add if candidate is >= last element to avoid duplicates
                        # This ensures combinations are in non-decreasing order
                        if not combination or candidate >= combination[-1]:
                            dp[num].append(combination + [candidate])
        
        return dp[target]

def run_combination_sum_tests():
    """Run comprehensive unit tests for the Combination Sum solution."""
    
    print("Running Unit Tests for Combination Sum...")
    sol = Solution()
    
    # Test Case 1: Basic case
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = sol.combinationSum(candidates1, target1)
    expected1 = [[2, 2, 3], [7]]
    # Sort results for comparison
    result1_sorted = [sorted(combo) for combo in result1]
    result1_sorted.sort()
    expected1_sorted = [sorted(combo) for combo in expected1]
    expected1_sorted.sort()
    assert result1_sorted == expected1_sorted, f"Test 1 failed: Expected {expected1_sorted}, got {result1_sorted}"
    print("✓ Test 1 Passed: [2,3,6,7], target=7 → [[2,2,3], [7]]")
    
    # Test Case 2: Smaller case
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = sol.combinationSum(candidates2, target2)
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result2_sorted = [sorted(combo) for combo in result2]
    result2_sorted.sort()
    expected2_sorted = [sorted(combo) for combo in expected2]
    expected2_sorted.sort()
    assert result2_sorted == expected2_sorted, f"Test 2 failed: Expected {expected2_sorted}, got {result2_sorted}"
    print("✓ Test 2 Passed: [2,3,5], target=8 → [[2,2,2,2], [2,3,3], [3,5]]")
    
    # Test Case 3: Single candidate
    candidates3 = [2]
    target3 = 1
    result3 = sol.combinationSum(candidates3, target3)
    expected3 = []
    assert result3 == expected3, f"Test 3 failed: Expected {expected3}, got {result3}"
    print("✓ Test 3 Passed: [2], target=1 → []")
    
    # Test Case 4: Target equals candidate
    candidates4 = [1]
    target4 = 1
    result4 = sol.combinationSum(candidates4, target4)
    expected4 = [[1]]
    assert result4 == expected4, f"Test 4 failed: Expected {expected4}, got {result4}"
    print("✓ Test 4 Passed: [1], target=1 → [[1]]")
    
    # Test Case 5: Larger target
    candidates5 = [2, 3]
    target5 = 6
    result5 = sol.combinationSum(candidates5, target5)
    expected5 = [[2, 2, 2], [3, 3]]
    result5_sorted = [sorted(combo) for combo in result5]
    result5_sorted.sort()
    expected5_sorted = [sorted(combo) for combo in expected5]
    expected5_sorted.sort()
    assert result5_sorted == expected5_sorted, f"Test 5 failed: Expected {expected5_sorted}, got {result5_sorted}"
    print("✓ Test 5 Passed: [2,3], target=6 → [[2,2,2], [3,3]]")
    
    # Test Case 6: No valid combinations
    candidates6 = [5, 10, 15]
    target6 = 3
    result6 = sol.combinationSum(candidates6, target6)
    expected6 = []
    assert result6 == expected6, f"Test 6 failed: Expected {expected6}, got {result6}"
    print("✓ Test 6 Passed: [5,10,15], target=3 → []")
    
    # Test Case 7: Multiple valid combinations
    candidates7 = [1, 2, 3]
    target7 = 4
    result7 = sol.combinationSum(candidates7, target7)
    expected7 = [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3]]
    result7_sorted = [sorted(combo) for combo in result7]
    result7_sorted.sort()
    expected7_sorted = [sorted(combo) for combo in expected7]
    expected7_sorted.sort()
    assert result7_sorted == expected7_sorted, f"Test 7 failed: Expected {expected7_sorted}, got {result7_sorted}"
    print("✓ Test 7 Passed: [1,2,3], target=4 → [[1,1,1,1], [1,1,2], [2,2], [1,3]]")
    
    # Test Case 8: All elements can be used multiple times
    candidates8 = [7]
    target8 = 7
    result8 = sol.combinationSum(candidates8, target8)
    expected8 = [[7]]
    assert result8 == expected8, f"Test 8 failed: Expected {expected8}, got {result8}"
    print("✓ Test 8 Passed: [7], target=7 → [[7]]")
    
    # Test Case 9: Verify no duplicates in result
    candidates9 = [2, 3, 6, 7]
    target9 = 7
    result9 = sol.combinationSum(candidates9, target9)
    # Check that no duplicate combinations exist
    result9_tuples = [tuple(sorted(combo)) for combo in result9]
    unique_result = list(set(result9_tuples))
    assert len(result9_tuples) == len(unique_result), f"Test 9 failed: Found duplicates in result {result9}"
    print("✓ Test 9 Passed: No duplicates in result")
    
    # Test Case 10: Verify each combination sums to target
    candidates10 = [2, 3, 5, 7]
    target10 = 10
    result10 = sol.combinationSum(candidates10, target10)
    for combo in result10:
        assert sum(combo) == target10, f"Test 10 failed: Combination {combo} doesn't sum to {target10}"
    print("✓ Test 10 Passed: All combinations sum to target")
    
    print("\n🎉 All Combination Sum tests passed! The solution works correctly.")

def explain_combination_sum_algorithm():
    """Explain the Combination Sum algorithm in detail."""
    
    print("\n" + "="*70)
    print("COMBINATION SUM ALGORITHM EXPLANATION")
    print("="*70)
    
    print("\nWhat is Combination Sum?")
    print("-" * 30)
    print("Given an array of distinct integers and a target, find all unique combinations")
    print("where candidate numbers sum to the target. Each number may be used unlimited times.")
    
    print("\nAlgorithm Approach: Dynamic Programming")
    print("-" * 40)
    print("The solution uses bottom-up dynamic programming:")
    print("• dp[i] stores all combinations that sum to i")
    print("• Build solutions for larger targets from smaller ones")
    
    print("\nKey Steps:")
    print("-" * 20)
    print("1. Sort candidates for ordered processing and early termination")
    print("2. Initialize dp array with empty lists")
    print("3. For each target value from 0 to target:")
    print("   - Try each candidate")
    print("   - If candidate equals current target, add as single-element combination")
    print("   - If candidate is smaller, combine with existing solutions")
    print("   - Maintain non-decreasing order to avoid duplicates")
    
    print("\nAvoiding Duplicates:")
    print("-" * 30)
    print("The algorithm prevents duplicate combinations by ensuring:")
    print("• New elements added to combinations are >= last element in the existing combination")
    print("• This maintains non-decreasing order throughout")
    print("• [2,3] and [3,2] are prevented - only [2,3] is generated")
    
    print("\nDetailed Example: candidates=[2,3], target=5")
    print("-" * 45)
    print("dp[0] = []")
    print("dp[1] = []")
    print("dp[2] = [[2]] (direct match)")
    print("dp[3] = [[3]] (direct match)")
    print("dp[4] = [[2,2]] (from dp[2] + [2])")
    print("dp[5] = [[2,3]] (from dp[2] + [3])")
    print("Result: [[2,3]]")
    
    print("\nTime & Space Complexity:")
    print("-" * 30)
    print("Time: O(N^(T/M)) where N=number of candidates, T=target, M=min(candidates)")
    print("Space: O(N^(T/M)) for storing all combinations")
    print("• In worst case, exponential number of combinations may exist")
    
    print("\nWhy Sorting Helps:")
    print("-" * 30)
    print("• Enables early termination when candidates exceed current target")
    print("• Facilitates the non-decreasing order constraint")
    print("• Makes algorithm more efficient by avoiding unnecessary checks")
    
    print("\nAlgorithm Properties:")
    print("-" * 30)
    print("• Generates all valid combinations (completeness)")
    print("• No duplicates (uniqueness)")
    print("• Each number can be reused unlimited times")
    print("• Efficient due to DP memoization of subproblems")
    
    print("\nAlternative Approaches:")
    print("-" * 30)
    print("• Backtracking: More intuitive, naturally avoids duplicates")
    print("• DFS: Similar to backtracking, explores solution space systematically")
    print("• DP: Efficient for multiple queries with same candidates")

if __name__ == "__main__":
    # Run tests
    run_combination_sum_tests()
    
    # Explain the algorithm
    explain_combination_sum_algorithm()