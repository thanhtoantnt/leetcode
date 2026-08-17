import math

from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverses the digits of a signed 32-bit integer.
        
        Problem Understanding:
        - Given a signed 32-bit integer x, return x with its digits reversed.
        - If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], return 0.
        - The environment does not allow storing 64-bit integers (signed or unsigned).
        
        Approach:
        - Define the 32-bit signed integer limits (MIN and MAX).
        - Initialize a result variable (res) to 0.
        - Iterate while x is not zero:
            - Extract the last digit using fmod(x, 10). This handles negative numbers correctly,
              unlike the standard modulo operator in some other languages when dealing with negatives.
              The result is cast to int to get the digit value.
            - Remove the last digit from x using int(x / 10). This truncates towards zero, which is
              necessary for handling negative numbers correctly in the loop condition.
            - Check for potential overflow before updating the result (res * 10 + digit).
              - Check if `res > MAX // 10`. If so, `res * 10` will definitely exceed MAX.
              - Check if `res == MAX // 10` and `digit > MAX % 10`. If so, `res * 10 + digit` will exceed MAX.
              - Check if `res < MIN // 10`. If so, `res * 10` will definitely be less than MIN.
              - Check if `res == MIN // 10` and `digit < MIN % 10`. If so, `res * 10 + digit` will be less than MIN.
              - If any overflow condition is met, return 0 immediately.
            - If no overflow, update the result: res = (res * 10) + digit.
        - Return the final result.
        - This approach avoids performing the potentially overflowing operation `res * 10 + digit`
          directly during the check, using integer division and modulo on the limits instead.
        
        Time Complexity: O(log x) where x is the input number. The number of digits is proportional to log10(x).
        Space Complexity: O(1). Only a constant amount of extra space is used.
        
        Args:
            x: The signed 32-bit integer to reverse.
            
        Returns:
            The reversed integer, or 0 if the result overflows.
        """
        MIN = -2147483648  # -2^31
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            # Extract the last digit using fmod to handle negatives correctly
            digit = int(math.fmod(x, 10))
            # Remove the last digit using integer division that truncates towards zero
            x = int(x / 10)

            # Check for potential overflow before updating res
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            
            # Build the reversed number
            res = (res * 10) + digit

        return res

def run_reverse_integer_test(x, expected, test_name):
    """
    Tests the reverse function.
    
    Args:
        x: Input integer to be reversed
        expected: Expected reversed integer
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.reverse(x)
    
    print(f"{test_name}:")
    print(f"  Input: {x}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_reverse_integer_test(123, 321, "Example 1: Positive number")
run_reverse_integer_test(-123, -321, "Example 2: Negative number")
run_reverse_integer_test(120, 21, "Example 3: Number ending in zero")
run_reverse_integer_test(1534236469, 0, "Edge case: Overflow (positive)")
run_reverse_integer_test(-2147483648, 0, "Edge case: Input is INT_MIN (would overflow on reversal)")
run_reverse_integer_test(2147483647, 0, "Edge case: Input is INT_MAX (would overflow on reversal)")
run_reverse_integer_test(0, 0, "Edge case: Zero input")
run_reverse_integer_test(7, 7, "Edge case: Single positive digit")
run_reverse_integer_test(-7, -7, "Edge case: Single negative digit")
run_reverse_integer_test(100, 1, "Edge case: Number with trailing zeros after reversal")
run_reverse_integer_test(-100, -1, "Edge case: Negative number with trailing zeros after reversal")
