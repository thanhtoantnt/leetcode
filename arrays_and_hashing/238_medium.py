from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element at index i is the product of all elements 
        in the input array except nums[i].
        
        Problem Understanding:
        - Given an array of integers
        - For each position, calculate the product of all other numbers
        - Do not use division operation
        - Solve in O(n) time and O(1) extra space (output array doesn't count)
        
        Approach:
        - First pass: Calculate left products (product of all elements to the left)
        - Second pass: Calculate right products and multiply with left products
        - Use the result array to store intermediate calculations
        
        Time Complexity: O(n) where n is the length of the array
        Space Complexity: O(1) extra space (excluding output array)
        
        Args:
            nums: List of integers
            
        Returns:
            Array where each element is the product of all other elements
        """
        # Initialize result array with 1s
        # This will eventually hold the final answer
        result = [1] * len(nums)

        # First pass: Calculate left products
        # For each index i, result[i] will contain product of elements to the left
        mul = 1  # Running product of elements to the left
        for index, num in enumerate(nums):
            result[index] = mul  # Store product of elements to the left
            mul = mul * num      # Update running product

        # Second pass: Calculate right products and multiply with left products
        # For each index i, multiply left product with right product
        mul = 1  # Running product of elements to the right
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= mul  # Multiply left product with right product
            mul = mul * nums[index]  # Update running product of elements to the right

        return result

def run_product_test(nums, expected, test_name):
    """
    Tests the productExceptSelf function.
    
    Args:
        nums: Input list of integers
        expected: Expected result array
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.productExceptSelf(nums)
    
    print(f"{test_name}:")
    print(f"  Input: {nums}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_product_test([1,2,3,4], [24,12,8,6], "Example 1: Basic case")
run_product_test([-1,1,0,-3,3], [0,0,9,0,0], "Example 2: With zeros and negatives")
run_product_test([2,3,4,5], [60,40,30,24], "Edge case: All positive")
run_product_test([-2,-3,-4,-5], [-60,-40,-30,-24], "Edge case: All negative")
run_product_test([0,1,2,3], [6,0,0,0], "Edge case: Single zero")
run_product_test([0,0,1,2], [0,0,0,0], "Edge case: Multiple zeros")
run_product_test([1], [1], "Edge case: Single element")
run_product_test([1,0], [0], "Edge case: Two elements with zero")
run_product_test([2,3], [3,2], "Edge case: Two elements without zero")
run_product_test([1,-1,2,-2], [4,-4,-2,2], "Edge case: Alternating signs")