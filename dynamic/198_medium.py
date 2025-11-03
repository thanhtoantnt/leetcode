from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Finds the maximum amount of money that can be robbed without alerting the police.
        
        Problem Understanding:
        - You are a robber planning to rob houses along a street
        - Each house has a certain amount of money
        - Adjacent houses have security systems connected
        - If two adjacent houses are robbed, the system will automatically contact the police
        - Find the maximum amount of money that can be robbed without alerting the police
        
        Approach:
        - Use dynamic programming with state: dp[i] = max money that can be robbed up to house i
        - At each house, decide whether to rob it or not:
          - If rob current house: money = nums[i] + dp[i-2] (can't rob previous)
          - If don't rob current house: money = dp[i-1] (take previous max)
        - Take maximum of both options
        - Can optimize space to O(1) by keeping only previous two values
        
        Time Complexity: O(n) where n is length of nums
        Space Complexity: O(1) - constant extra space
        
        Args:
            nums: List of integers representing money in each house
            
        Returns:
            Maximum amount that can be robbed without alerting police
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        # Use variables to track previous two values (space optimization)
        prev2 = nums[0]  # Max money up to house 0
        prev1 = max(nums[0], nums[1])  # Max money up to house 1
        
        # For each house starting from index 2
        for i in range(2, len(nums)):
            # Current max = max(rob current house + max up to i-2, don't rob current + max up to i-1)
            current = max(nums[i] + prev2, prev1)
            prev2 = prev1
            prev1 = current
        
        return prev1

def run_house_robber_test(nums, expected, test_name):
    """
    Tests the rob function.
    
    Args:
        nums: List of integers representing money in each house
        expected: Expected maximum amount that can be robbed
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.rob(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_house_robber_test([1,2,3,1], 4, "Example 1: [1,2,3,1] -> 4 (rob house 0 and 2: 1+3=4)")
run_house_robber_test([2,7,9,3,1], 12, "Example 2: [2,7,9,3,1] -> 12 (rob house 0, 2, and 4: 2+9+1=12)")
run_house_robber_test([1], 1, "Edge case: Single house [1] -> 1")
run_house_robber_test([1,2], 2, "Edge case: Two houses [1,2] -> 2")
run_house_robber_test([2,1], 2, "Edge case: Two houses [2,1] -> 2")
run_house_robber_test([2,1,1,2], 4, "Edge case: [2,1,1,2] -> 4 (rob house 0 and 3: 2+2=4)")
run_house_robber_test([1,2,3,4,5], 9, "Edge case: [1,2,3,4,5] -> 9 (rob house 1 and 3: 2+4=6 or house 0,2,4: 1+3+5=9)")
run_house_robber_test([5,1,3,5], 10, "Edge case: [5,1,3,5] -> 10 (rob house 0 and 3: 5+5=10)")
run_house_robber_test([1,2,1,1], 3, "Edge case: [1,2,1,1] -> 3 (rob house 1 and 3: 2+1=3)")
run_house_robber_test([2,1,1,1,2], 5, "Edge case: [2,1,1,1,2] -> 5 (rob house 0, 2, and 4: 2+1+2=5)")
run_house_robber_test([0], 0, "Edge case: Single house with 0 [0] -> 0")
run_house_robber_test([0,0,0,0], 0, "Edge case: All zeros -> 0")