from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Finds the length of the longest strictly increasing subsequence.
        
        Problem Understanding:
        - Given an integer array nums
        - Return the length of the longest strictly increasing subsequence
        - Subsequence maintains relative order but doesn't need to be contiguous
        
        Approach:
        - Use dynamic programming with binary search for O(n log n) solution
        - Maintain an array 'tails' where tails[i] is the smallest ending element of all increasing subsequences of length i+1
        - For each number, find its position in tails using binary search
        - If number is larger than all elements in tails, append it (extend LIS)
        - Otherwise, replace the first element that is >= current number
        - Length of tails array is the length of LIS
        
        Time Complexity: O(n log n) where n is length of nums
        Space Complexity: O(n) for the tails array
        
        Args:
            nums: List of integers
            
        Returns:
            Length of the longest increasing subsequence
        """
        if not nums:
            return 0
        
        # tails[i] = smallest ending element of all increasing subsequences of length i+1
        tails = []
        
        for num in nums:
            # Binary search to find the position to insert/replace
            left, right = 0, len(tails)
            
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            # If num is larger than all elements in tails, append it
            if left == len(tails):
                tails.append(num)
            else:
                # Replace the element at position 'left' with num
                tails[left] = num
        
        return len(tails)

def run_lis_test(nums, expected, test_name):
    """
    Tests the lengthOfLIS function.
    
    Args:
        nums: List of integers
        expected: Expected length of longest increasing subsequence
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.lengthOfLIS(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_lis_test([10,9,2,5,3,7,101,18], 4, "Example 1: [10,9,2,5,3,7,101,18] -> 4 (subsequence [2,3,7,18])")
run_lis_test([0,1,0,3,2,3], 4, "Example 2: [0,1,0,3,2,3] -> 4 (subsequence [0,1,2,3])")
run_lis_test([7,7,7,7,7,7,7], 1, "Example 3: [7,7,7,7,7,7,7] -> 1")
run_lis_test([1,3,6,7,9,4,10,5,6], 6, "Edge case: [1,3,6,7,9,4,10,5,6] -> 6")
run_lis_test([1], 1, "Edge case: Single element [1] -> 1")
run_lis_test([], 0, "Edge case: Empty array -> 0")
run_lis_test([1,2,3,4,5], 5, "Edge case: Strictly increasing [1,2,3,4,5] -> 5")
run_lis_test([5,4,3,2,1], 1, "Edge case: Strictly decreasing [5,4,3,2,1] -> 1")
run_lis_test([1,3,2,4], 3, "Edge case: [1,3,2,4] -> 3 (subsequence [1,2,4] or [1,3,4])")
run_lis_test([2,1,3,4], 3, "Edge case: [2,1,3,4] -> 3 (subsequence [1,3,4])")
run_lis_test([1,2,1,2,1,2], 2, "Edge case: Alternating [1,2,1,2,1,2] -> 2")
run_lis_test([4,10,4,3,8,9], 3, "Edge case: [4,10,4,3,8,9] -> 3 (subsequence [4,8,9] or [3,8,9])")