from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Returns all possible subsets of the given array that may contain duplicates.
        
        Problem Understanding:
        - Given an integer array that may contain duplicates
        - Return all possible subsets (the power set)
        - The solution set must not contain duplicate subsets
        - Return the solution in any order
        
        Approach:
        - Use backtracking with sorted array to handle duplicates
        - Sort the input array to group duplicates together
        - At each recursion level, skip duplicate elements to avoid duplicate subsets
        - For each unique element, decide whether to include it or not
        
        Time Complexity: O(2^N) where N is the length of nums (worst case without duplicates)
        Space Complexity: O(N) for recursion depth (excluding output)
        
        Args:
            nums: List of integers (may contain duplicates)
            
        Returns:
            List of all possible unique subsets
        """
        # Sort the array to group duplicates together
        nums.sort()
        result = []
        
        def backtrack(start, current_subset):
            # Add current subset to result (make a copy)
            result.append(current_subset[:])
            
            # Explore further elements to add to subset
            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                # If current element is same as previous and previous was at the same level (i > start),
                # then we've already considered this combination
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                # Include nums[i] in current subset
                current_subset.append(nums[i])
                
                # Recursively generate subsets starting from next element
                backtrack(i + 1, current_subset)
                
                # Backtrack: remove nums[i] to try other possibilities
                current_subset.pop()
        
        backtrack(0, [])
        return result

def run_subsets_with_dup_test(nums, expected, test_name):
    """
    Tests the subsetsWithDup function.
    
    Args:
        nums: Input list of integers (may contain duplicates)
        expected: Expected list of all unique subsets
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.subsetsWithDup(nums)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(sorted(subset)) for subset in result)
    expected_set = set(tuple(sorted(subset)) for subset in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_subsets_with_dup_test([1,2,2], [[],[1],[1,2],[1,2,2],[2],[2,2]], "Example 1: [1,2,2] -> [[],[1],[1,2],[1,2,2],[2],[2,2]]")
run_subsets_with_dup_test([0], [[],[0]], "Example 2: [0] -> [[],[0]]")
run_subsets_with_dup_test([4,4,4,1,4], [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]], "Edge case: Multiple duplicates [4,4,4,1,4]")
run_subsets_with_dup_test([1,2,3], [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]], "Edge case: No duplicates [1,2,3] -> all 8 subsets")
run_subsets_with_dup_test([1,1,1], [[],[1],[1,1],[1,1,1]], "Edge case: All same [1,1,1] -> [[],[1],[1,1],[1,1,1]]")
run_subsets_with_dup_test([], [[]], "Edge case: Empty array -> [[]]")
run_subsets_with_dup_test([1,1], [[],[1],[1,1]], "Edge case: Two same [1,1] -> [[],[1],[1,1]]")
run_subsets_with_dup_test([1,2,2,3], [[],[1],[1,2],[1,2,2],[1,2,2,3],[1,2,3],[1,3],[2],[2,2],[2,2,3],[2,3],[3]], "Edge case: [1,2,2,3] -> unique subsets")
run_subsets_with_dup_test([5,5,5,5,5], [[],[5],[5,5],[5,5,5],[5,5,5,5],[5,5,5,5,5]], "Edge case: All same [5,5,5,5,5] -> [[],[5],[5,5],[5,5,5],[5,5,5,5],[5,5,5,5,5]]")
run_subsets_with_dup_test([1,2,1], [[],[1],[1,1],[1,1,2],[1,2],[2]], "Edge case: [1,2,1] -> [[],[1],[1,1],[1,1,2],[1,2],[2]]")