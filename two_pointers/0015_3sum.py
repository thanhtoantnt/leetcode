from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array which gives the sum of zero.
        
        Problem Understanding:
        - Given an integer array, find all unique triplets [nums[i], nums[j], nums[k]]
        - Such that i != j, i != k, j != k and nums[i] + nums[j] + nums[k] == 0
        - Return results without duplicate triplets
        
        Approach:
        - Sort the array to enable two-pointer technique and duplicate skipping
        - Fix first number using outer loop
        - Use two pointers for remaining two numbers to find sum = -first_number
        - Skip duplicates at each level to ensure uniqueness
        - Two-pointer search for the remaining sum after fixing first number
        
        Time Complexity: O(n²) where n is the length of the array
        Space Complexity: O(1) excluding the output array (not counting space for output)
        
        Args:
            nums: List of integers
            
        Returns:
            List of unique triplets that sum to zero
        """
        # Sort array to enable two-pointer technique and duplicate detection
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n-2):  # Need at least 2 more elements after i
            # Skip duplicates for first number to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Two pointers for remaining two numbers
            left = i + 1
            right = n - 1
            target = -nums[i]  # Need nums[left] + nums[right] = target

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum == target:
                    # Found valid triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers to find next unique combination
                    left += 1
                    right -= 1

                elif current_sum < target:
                    # Sum too small, move left pointer right to increase sum
                    left += 1
                else:
                    # Sum too large, move right pointer left to decrease sum
                    right -= 1

        return result

def run_three_sum_test(nums, expected, test_name):
    """
    Tests the threeSum function with set-based comparison.
    
    Args:
        nums: Input list of integers
        expected: Expected list of triplets
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.threeSum(nums)
    
    # Convert to sets of tuples for order-independent comparison
    result_set = set(tuple(sorted(triplet)) for triplet in result)
    expected_set = set(tuple(sorted(triplet)) for triplet in expected)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print()

# Run test cases
run_three_sum_test([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]], "Example 1: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]")
run_three_sum_test([0,1,1], [], "Example 2: [0,1,1] -> [] (no valid triplets)")
run_three_sum_test([0,0,0], [[0,0,0]], "Example 3: [0,0,0] -> [[0,0,0]]")
run_three_sum_test([0,0,0,0], [[0,0,0]], "Edge case: Multiple zeros")
run_three_sum_test([-2,0,1,1,2], [[-2,0,2],[-2,1,1]], "Edge case: [-2,0,1,1,2] -> [[-2,0,2],[-2,1,1]]")
run_three_sum_test([1,2,-2,-1], [], "Edge case: No valid triplets")
run_three_sum_test([3,-2,1,0], [], "Edge case: No valid triplets")
run_three_sum_test([-1,0,1,0], [[-1,0,1]], "Edge case: [-1,0,1,0] -> [[-1,0,1]]")
run_three_sum_test([1,-1,-1,0], [[-1,0,1]], "Edge case: [-1,-1,0,1] -> [[-1,0,1]]")
run_three_sum_test([], [], "Edge case: Empty array")
run_three_sum_test([1,2], [], "Edge case: Less than 3 elements")
run_three_sum_test([1,-1,0], [[-1,0,1]], "Edge case: Exactly 3 elements with valid triplet")
run_three_sum_test([-1,0,1,2,-1,-4,-1,2], [[-1,-1,2],[-1,0,1]], "Edge case: Many duplicates")