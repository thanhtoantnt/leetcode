from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Finds the number of ways to assign '+' or '-' to each number to reach target sum.
        
        Problem Understanding:
        - Given an integer array nums and integer target
        - Add '+' or '-' sign before each integer and concatenate all integers
        - Return the number of different expressions that evaluate to target
        
        Approach:
        - Transform the problem: let P be the set of numbers with '+' and N be the set with '-'
        - Then sum(P) - sum(N) = target
        - Also sum(P) + sum(N) = total_sum
        - Solving these equations: sum(P) = (total_sum + target) / 2
        - This becomes a subset sum problem: find number of ways to select numbers that sum to (total_sum + target) / 2
        - Use dynamic programming similar to coin change but counting combinations
        
        Time Complexity: O(n * sum) where n is length of nums and sum is total sum
        Space Complexity: O(sum) for the DP array
        
        Args:
            nums: List of non-negative integers
            target: Target sum to achieve
            
        Returns:
            Number of ways to assign signs to reach target
        """
        total_sum = sum(nums)
        
        # Check if target is achievable
        # (total_sum + target) must be even and non-negative
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        # Calculate the subset sum we need to find
        subset_sum = (total_sum + target) // 2
        
        # DP array: dp[i] = number of ways to achieve sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # One way to achieve sum 0: select no elements
        
        # For each number in nums
        for num in nums:
            # Iterate backwards to avoid using the same number multiple times in one combination
            for current_sum in range(subset_sum, num - 1, -1):
                dp[current_sum] += dp[current_sum - num]
        
        return dp[subset_sum]

def run_target_sum_test(nums, target, expected, test_name):
    """
    Tests the findTargetSumWays function.
    
    Args:
        nums: List of non-negative integers
        target: Target sum to achieve
        expected: Expected number of ways
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findTargetSumWays(nums, target)
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_target_sum_test([1,1,1,1,1], 3, 5, "Example 1: [1,1,1,1,1], target=3 -> 5 ways")
run_target_sum_test([1], 1, 1, "Example 2: [1], target=1 -> 1 way")
run_target_sum_test([1,0], 1, 2, "Edge case: [1,0], target=1 -> 2 ways")
run_target_sum_test([0,0,0,0,0,0,0,0,1], 1, 256, "Edge case: Zeros with one 1 -> 256 ways")
run_target_sum_test([1,2,7,9,981], 1000000000, 0, "Edge case: Impossible target -> 0 ways")
run_target_sum_test([0], 0, 2, "Edge case: [0], target=0 -> 2 ways (+0 and -0)")
run_target_sum_test([1,2], 3, 1, "Edge case: [1,2], target=3 -> 1 way (+1+2)")
run_target_sum_test([1,2], 1, 1, "Edge case: [1,2], target=1 -> 1 way (+1-2 or -1+2) -> Actually +1-2=1, -1+2=1")
run_target_sum_test([1,1,1,1,1], 1, 5, "Edge case: [1,1,1,1,1], target=1 -> 5 ways")
run_target_sum_test([1,2,3], 0, 2, "Edge case: [1,2,3], target=0 -> 2 ways")
run_target_sum_test([1,2,3,4], 6, 2, "Edge case: [1,2,3,4], target=6 -> 2 ways")
run_target_sum_test([1,2,3,4,5], 3, 4, "Edge case: [1,2,3,4,5], target=3 -> 4 ways")