from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Returns all possible permutations of the given array.
        
        Problem Understanding:
        - Given an array of distinct integers
        - Return all possible permutations (arrangements) of the elements
        - Each permutation is a rearrangement of all elements
        
        Approach:
        - Use backtracking to build permutations incrementally
        - At each position, try each unused number
        - Use a set or boolean array to track which numbers are already used
        - When permutation length equals input length, add to result
        - Backtrack by removing the last added number and marking it as unused
        
        Time Complexity: O(N! * N) where N is the length of nums
        Space Complexity: O(N) for recursion depth and used set (excluding output)
        
        Args:
            nums: List of distinct integers
            
        Returns:
            List of all possible permutations
        """
        result = []
        used = set()
        
        def backtrack(current_permutation):
            # Base case: if current permutation has same length as input, we found a permutation
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])  # Add a copy of current permutation
                return
            
            # Try each number that hasn't been used yet
            for num in nums:
                if num not in used:
                    # Add current number to permutation
                    current_permutation.append(num)
                    used.add(num)
                    
                    # Recursively build the rest of the permutation
                    backtrack(current_permutation)
                    
                    # Backtrack: remove the last added number and mark as unused
                    current_permutation.pop()
                    used.remove(num)
        
        backtrack([])
        return result

def run_permute_test(nums, expected, test_name):
    """
    Tests the permute function.
    
    Args:
        nums: Input list of distinct integers
        expected: Expected list of all permutations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.permute(nums)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(perm) for perm in result)
    expected_set = set(tuple(perm) for perm in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_permute_test([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], "Example 1: [1,2,3] -> all 6 permutations")
run_permute_test([0,1], [[0,1],[1,0]], "Example 2: [0,1] -> all 2 permutations")
run_permute_test([1], [[1]], "Example 3: [1] -> single permutation")
run_permute_test([1,2,3,4], [[1,2,3,4],[1,2,4,3],[1,3,2,4],[1,3,4,2],[1,4,2,3],[1,4,3,2],[2,1,3,4],[2,1,4,3],[2,3,1,4],[2,3,4,1],[2,4,1,3],[2,4,3,1],[3,1,2,4],[3,1,4,2],[3,2,1,4],[3,2,4,1],[3,4,1,2],[3,4,2,1],[4,1,2,3],[4,1,3,2],[4,2,1,3],[4,2,3,1],[4,3,1,2],[4,3,2,1]], "Edge case: [1,2,3,4] -> all 24 permutations")
run_permute_test([], [[]], "Edge case: Empty array -> [[]]")
run_permute_test([5], [[5]], "Edge case: Single element [5] -> [[5]]")
run_permute_test([1,2], [[1,2],[2,1]], "Edge case: Two elements [1,2] -> [[1,2],[2,1]]")
run_permute_test([-1,1], [[-1,1],[1,-1]], "Edge case: Negative numbers [-1,1] -> [[-1,1],[1,-1]]")