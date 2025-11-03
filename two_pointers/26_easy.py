from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from a sorted array in-place such that each unique element appears only once.
        
        Problem Understanding:
        - Given a sorted array, remove duplicates in-place
        - Return the number of unique elements
        - The first k elements should contain the unique elements in their original order
        - Other elements can be anything
        
        Approach:
        - Use two pointers: one for reading (i), one for writing (j)
        - Read pointer traverses the array
        - Write pointer keeps track of where to place next unique element
        - When we find a new unique element (different from previous), place it at write pointer
        - Return the position of write pointer (count of unique elements)
        
        Time Complexity: O(n) where n is the length of nums array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            nums: Sorted array of integers
            
        Returns:
            Number of unique elements in the array
        """
        if not nums:
            return 0
        
        # Write pointer starts at 1 (first element is always unique)
        write_pos = 1
        
        # Read from second element
        for read_pos in range(1, len(nums)):
            # If current element is different from previous unique element
            if nums[read_pos] != nums[read_pos - 1]:
                # Place it at write position
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos

def run_remove_duplicates_test(nums, expected_k, expected_nums, test_name):
    """
    Tests the removeDuplicates function.
    
    Args:
        nums: Input array (will be modified in-place)
        expected_k: Expected number of unique elements
        expected_nums: Expected first k elements after removal
        test_name: Name/description of the test case
    """
    original_nums = nums[:]  # Make a copy to preserve original
    solution = Solution()
    result_k = solution.removeDuplicates(nums)
    
    # Check the first k elements
    actual_first_k = nums[:result_k]
    
    print(f"{test_name}:")
    print(f"  Input: {original_nums}")
    print(f"  Expected k: {expected_k}, Expected first k: {expected_nums}")
    print(f"  Got k: {result_k}, Got first k: {actual_first_k}")
    print(f"  k matches: {result_k == expected_k}")
    print(f"  First k elements match: {actual_first_k == expected_nums}")
    print(f"  Pass: {result_k == expected_k and actual_first_k == expected_nums}")
    print()

# Run test cases
run_remove_duplicates_test([1,1,2], 2, [1,2], "Example 1: [1,1,2] -> k=2, [1,2,_]")
run_remove_duplicates_test([0,0,1,1,1,2,2,3,3,4], 5, [0,1,2,3,4], "Example 2: [0,0,1,1,1,2,2,3,3,4] -> k=5, [0,1,2,3,4,_]")
run_remove_duplicates_test([1], 1, [1], "Edge case: Single element [1] -> k=1, [1]")
run_remove_duplicates_test([1,1,1,1], 1, [1], "Edge case: All same [1,1,1,1] -> k=1, [1]")
run_remove_duplicates_test([1,2,3,4,5], 5, [1,2,3,4,5], "Edge case: No duplicates [1,2,3,4,5] -> k=5, [1,2,3,4,5]")
run_remove_duplicates_test([1,1,2,2,3,3], 3, [1,2,3], "Edge case: Pairs [1,1,2,2,3,3] -> k=3, [1,2,3]")
run_remove_duplicates_test([1,2,1,2,1,2], 2, [1,2], "Edge case: Alternating [1,2,1,2,1,2] -> k=2, [1,2]")
run_remove_duplicates_test([1,1,1,2,2,3], 3, [1,2,3], "Edge case: [1,1,1,2,2,3] -> k=3, [1,2,3]")
run_remove_duplicates_test([], 0, [], "Edge case: Empty array [] -> k=0, []")
run_remove_duplicates_test([1,2,3,4,5,6,7,8,9,10], 10, [1,2,3,4,5,6,7,8,9,10], "Edge case: Sequential [1,2,3,4,5,6,7,8,9,10] -> k=10")