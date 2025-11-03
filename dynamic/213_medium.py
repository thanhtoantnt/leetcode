from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Finds the maximum amount of money that can be robbed from houses arranged in a circle.
        
        Problem Understanding:
        - Houses are arranged in a circle (first and last are adjacent)
        - Adjacent houses have security systems connected
        - If two adjacent houses are robbed, the system will automatically contact the police
        - The first house is adjacent to the last house
        - Find the maximum amount that can be robbed without alerting the police
        
        Approach:
        - Since first and last houses are adjacent, we have two scenarios:
          1. Rob houses from 0 to n-2 (excluding last house)
          2. Rob houses from 1 to n-1 (excluding first house)
        - Return the maximum of both scenarios
        - Use the same approach as House Robber I for each scenario
        - Handle edge cases for small arrays
        
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
        
        def rob_range(start, end):
            """Helper function to rob houses in a range [start, end]"""
            if start == end:
                return nums[start]
            if start + 1 == end:
                return max(nums[start], nums[end])
            
            # Use variables to track previous two values
            prev2 = nums[start]
            prev1 = max(nums[start], nums[start + 1])
            
            for i in range(start + 2, end + 1):
                current = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = current
            
            return prev1
        
        # Return maximum of two scenarios:
        # 1. Rob houses 0 to n-2 (can't rob both first and last)
        # 2. Rob houses 1 to n-1 (can't rob both first and last)
        return max(rob_range(0, len(nums) - 2), rob_range(1, len(nums) - 1))

def run_house_robber_ii_test(nums, expected, test_name):
    """
    Tests the rob function for circular arrangement.
    
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
run_house_robber_ii_test([2,3,2], 3, "Example 1: [2,3,2] -> 3 (rob house 1: 3)")
run_house_robber_ii_test([1,2,3,1], 4, "Example 2: [1,2,3,1] -> 4 (rob house 0 and 2: 1+3=4)")
run_house_robber_ii_test([1,2,3], 3, "Example 3: [1,2,3] -> 3 (rob house 2: 3)")
run_house_robber_ii_test([1], 1, "Edge case: Single house [1] -> 1")
run_house_robber_ii_test([1,2], 2, "Edge case: Two houses [1,2] -> 2")
run_house_robber_ii_test([2,1], 2, "Edge case: Two houses [2,1] -> 2")
run_house_robber_ii_test([1,3,1,3,100], 103, "Edge case: [1,3,1,3,100] -> 103 (rob house 1 and 4: 3+100=103)")
run_house_robber_ii_test([2,7,9,3,1], 11, "Edge case: [2,7,9,3,1] -> 11 (rob house 0, 2: 2+9=11)")
run_house_robber_ii_test([5,1,2,6], 7, "Edge case: [5,1,2,6] -> 7 (rob house 0 and 3: 5+2=7 or house 1 and 3: 1+6=7)")
run_house_robber_ii_test([4,1,2,7,5,3,1], 11, "Edge case: [4,1,2,7,5,3,1] -> 11")
run_house_robber_ii_test([0], 0, "Edge case: Single house with 0 [0] -> 0")
run_house_robber_ii_test([0,0,0,0], 0, "Edge case: All zeros -> 0")