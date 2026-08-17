from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
        
        Problem Understanding:
        - Convert a string to a 32-bit signed integer.
        - Ignore leading whitespace.
        - Check for an optional '+' or '-' sign.
        - Read digits until a non-digit character is encountered or the end of the string.
        - Skip leading zeros during digit reading.
        - Clamp the result to the 32-bit signed integer range [-2^31, 2^31 - 1].
          If the number is out of range, return INT_MIN (-2^31) or INT_MAX (2^31 - 1).
        
        Approach:
        - Strip leading whitespace from the string.
        - Determine the sign (+1 or -1) based on the first non-whitespace character.
          Default to positive if no sign is present.
        - Iterate through the characters starting from the first digit (or sign).
        - For each digit character, convert it to an integer and build the result.
        - Crucially, check for potential overflow/underflow *before* updating the result.
          If the current number is greater than (INT_MAX - digit) // 10, multiplying by 10
          and adding the digit would cause an overflow. Similarly, check for underflow.
        - If overflow would occur, return INT_MAX or INT_MIN based on the sign.
        - Return the final integer value with the determined sign applied.
        - This problem primarily involves string parsing and integer overflow handling,
          rather than standard bit manipulation operations like &, |, ^, <<, >>.
        
        Time Complexity: O(n) where n is the length of the input string 's'.
                         We iterate through the string at most once.
        Space Complexity: O(1). Only a constant amount of extra space is used.
        
        Args:
            s: The input string to convert.
            
        Returns:
            The converted 32-bit signed integer.
        """
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        i = 0
        n = len(s)

        # 1. Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Determine sign
        sign = 1
        if i < n and s[i] == '+':
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1

        # 3. Convert digits and build the number
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # 4. Check for overflow/underflow BEFORE updating result
            # If result > (INT_MAX - digit) // 10, then result * 10 + digit > INT_MAX
            # Since INT_MAX is positive, (INT_MAX - digit) // 10 is safe to calculate first.
            if sign == 1 and result > (INT_MAX - digit) // 10:
                return INT_MAX
            # If result > (INT_MIN - digit) // 10, then result * 10 + digit < INT_MIN
            # Since INT_MIN is negative, (INT_MIN - digit) // 10 might involve division of a negative number.
            # For negative numbers, we need to be careful. 
            # If sign is -1, we are effectively building a negative number.
            # We check if -result * 10 - digit < INT_MIN.
            # This is equivalent to checking if result > (abs(INT_MIN) - digit) // 10 when result represents
            # the positive magnitude being built. However, the check below is more direct:
            # We check if sign * (result * 10 + digit) would be < INT_MIN.
            # This translates to checking if sign is -1 and (result > (INT_MIN - (-digit)) // 10)
            # which is result > (INT_MIN + digit) // 10. 
            # Since we are building result as a positive number internally, and applying sign later,
            # the check becomes: if sign is -1 and the *positive* number we are building (result * 10 + digit)
            # exceeds the magnitude of INT_MIN, it will underflow.
            # So, if sign is -1 and result > (INT_MIN // 10) (where INT_MIN // 10 is -214748364)
            # or if result == (INT_MIN // 10) and digit > abs(INT_MIN % 10), it underflows.
            # INT_MIN % 10 is -8, so abs(INT_MIN % 10) is 8.
            if sign == -1 and (result > (INT_MIN // 10) or (result == (INT_MIN // 10) and digit > 8)):
                 return INT_MIN

            result = result * 10 + digit
            i += 1

        # Apply the sign and return the final result clamped within 32-bit range
        return sign * result

def run_my_atoi_test(s, expected, test_name):
    """
    Tests the myAtoi function.
    
    Args:
        s: Input string to be converted
        expected: Expected converted integer
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.myAtoi(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_my_atoi_test("42", 42, "Example 1: Simple positive number")
run_my_atoi_test(" -042", -42, "Example 2: Leading whitespace and negative sign")
run_my_atoi_test("1337c0d3", 1337, "Example 3: Number followed by non-digit")
run_my_atoi_test("0-1", 0, "Example 4: Number followed by non-digit (starting with zero)")
run_my_atoi_test("words and 987", 0, "Example 5: No leading number")
run_my_atoi_test("-91283472332", -2147483648, "Edge case: Underflow (INT_MIN)")
run_my_atoi_test("91283472332", 2147483647, "Edge case: Overflow (INT_MAX)")
run_my_atoi_test("   +0 123", 0, "Edge case: Leading spaces, sign, then non-digit")
run_my_atoi_test("+1", 1, "Edge case: Positive sign with single digit")
run_my_atoi_test("-", 0, "Edge case: Only a sign")
run_my_atoi_test("  ", 0, "Edge case: Only whitespace")
run_my_atoi_test("", 0, "Edge case: Empty string")
run_my_atoi_test("2147483647", 2147483647, "Edge case: Exactly INT_MAX")
run_my_atoi_test("-2147483648", -2147483648, "Edge case: Exactly INT_MIN")
run_my_atoi_test("  -0012a42", -12, "Edge case: Leading zeros, non-digit after")
run_my_atoi_test("   +45", 45, "Edge case: Leading spaces, positive sign")
