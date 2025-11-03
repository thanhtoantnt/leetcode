from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determines if the array can be partitioned into two subsets with equal sum.
        
        Problem Understanding:
        - Given an integer array nums
        - Return True if the array can be partitioned into two subsets with equal sum
        - Each element must belong to exactly one subset
        - This is equivalent to finding a subset with sum equal to half of total sum
        
        Approach:
        - First check if total sum is even (if odd, partition is impossible)
        - The problem becomes: find a subset with sum equal to total_sum // 2
        - Use dynamic programming with a set to track possible sums
        - For each number, update the set of possible sums by adding the current number to each existing sum
        - If we can achieve the target sum (total_sum // 2), return True
        
        Time Complexity: O(n * sum) where n is length of nums and sum is total sum
        Space Complexity: O(sum) for the possible sums set
        
        Args:
            nums: List of positive integers
            
        Returns:
            True if array can be partitioned into equal sum subsets, False otherwise
        """
        total_sum = sum(nums)
        
        # If total sum is odd, partition into equal subsets is impossible
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # If any number is greater than target, it's impossible
        if max(nums) > target:
            return False
        
        # Set to track all possible sums we can achieve
        possible_sums = {0}  # We can always achieve sum 0 (empty subset)
        
        for num in nums:
            # Create new possible sums by adding current number to each existing sum
            new_sums = set()
            for s in possible_sums:
                new_sum = s + num
                if new_sum == target:
                    return True  # Early termination if target is achieved
                if new_sum < target:  # Only keep sums that don't exceed target
                    new_sums.add(new_sum)
            
            # Add all new possible sums to our set
            possible_sums.update(new_sums)
        
        return target in possible_sums

def run_can_partition_test(nums, expected, test_name):
    """
    Tests the canPartition function.
    
    Args:
        nums: List of integers
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.canPartition(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_can_partition_test([1,5,11,5], True, "Example 1: [1,5,11,5] -> True (1,5,5 and 11)")
run_can_partition_test([1,2,3,5], False, "Example 2: [1,2,3,5] -> False")
run_can_partition_test([1,2,5], False, "Edge case: [1,2,5] -> False")
run_can_partition_test([1,2,3,4], True, "Edge case: [1,2,3,4] -> True (1,4 and 2,3)")
run_can_partition_test([1], False, "Edge case: Single element [1] -> False")
run_can_partition_test([1,1], True, "Edge case: [1,1] -> True")
run_can_partition_test([2,2,1,1], True, "Edge case: [2,2,1,1] -> True (2,1 and 2,1)")
run_can_partition_test([1,2,3,4,5,6], True, "Edge case: [1,2,3,4,5,6] -> True (1,4,5 and 2,3,6)")
run_can_partition_test([1,1,1,1], True, "Edge case: [1,1,1,1] -> True (1,1 and 1,1)")
run_can_partition_test([1,2,3,4,5,6,7,8], True, "Edge case: [1,2,3,4,5,6,7,8] -> True")
run_can_partition_test([100], False, "Edge case: Single large [100] -> False")
run_can_partition_test([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], True, "Edge case: Many same elements -> True")