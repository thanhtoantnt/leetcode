from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two distinct indices in the array whose values sum to the target.
        
        Problem Understanding:
        - Given an array of integers and a target sum
        - Find two different indices such that their values add up to target
        - Each input has exactly one solution
        - Cannot use the same element twice
        
        Approach:
        - Use hash map to store previously seen values and their indices
        - For each element, calculate its complement (target - current_value)
        - Check if complement exists in hash map
        - If yes, return the stored index and current index
        - If no, store current value and index in hash map
        - This is a "complement search" pattern
        
        Time Complexity: O(n) where n is the length of nums array
        Space Complexity: O(n) for the hash map storage
        
        Args:
            nums: List of integers
            target: Target sum to find
            
        Returns:
            List containing two indices whose values sum to target
        """
        # Hash map to store value -> index mapping
        hash_table = {}
        
        # Iterate through array with both index and value
        for index, number in enumerate(nums):
            # Calculate the complement needed to reach target
            complement = target - number
            
            # If complement exists in hash map, we found our pair
            if complement in hash_table:
                # Return [first_index, current_index]
                return [hash_table[complement], index]
            
            # Store current number and its index for future complement checks
            hash_table[number] = index
        
        # This should not be reached given the problem constraints
        return []

def run_two_sum_test(nums, target, expected, test_name):
    """
    Tests the twoSum function.
    
    Args:
        nums: Input list of integers
        target: Target sum to find
        expected: Expected pair of indices
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.twoSum(nums, target)
    
    # Verify the result by checking if the sum equals target
    valid_result = len(result) == 2 and result[0] != result[1] and nums[result[0]] + nums[result[1]] == target
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Valid (sums to target): {valid_result}")
    print(f"  Indices different: {len(result) >= 2 and result[0] != result[1] if len(result) >= 2 else False}")
    print()

# Run test cases
run_two_sum_test([2,7,11,15], 9, [0,1], "Example 1: [2,7,11,15], target=9 -> [0,1] (2+7=9)")
run_two_sum_test([3,2,4], 6, [1,2], "Example 2: [3,2,4], target=6 -> [1,2] (2+4=6)")
run_two_sum_test([3,3], 6, [0,1], "Example 3: [3,3], target=6 -> [0,1] (3+3=6)")
run_two_sum_test([1,2,3,4,5], 8, [2,4], "Edge case: [1,2,3,4,5], target=8 -> [2,4] (3+5=8)")
run_two_sum_test([1,5,3,7,9], 12, [2,3], "Edge case: [1,5,3,7,9], target=12 -> [2,3] (3+9=12 or 5+7=12)")
run_two_sum_test([-1,-2,-3,-4,-5], -8, [2,4], "Edge case: Negative numbers, target=-8")
run_two_sum_test([0,4,3,0], 0, [0,3], "Edge case: Zeros in array, target=0")
run_two_sum_test([1,2], 3, [0,1], "Edge case: Two elements, target=3")
run_two_sum_test([1,1,1,1,1,2], 3, [4,5], "Edge case: Multiple same values, target=3")
run_two_sum_test([-3,4,3,9], 0, [0,2], "Edge case: Negative and positive mix, target=0")