from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Converts a string into a zigzag pattern on a given number of rows and reads it line by line.
        
        Problem Understanding:
        - Given a string 's' and an integer 'numRows'
        - Arrange the string in a zigzag pattern down and up diagonally
        - Read the characters row by row to form the new string
        - Example: "PAYPALISHIRING" with numRows=3 becomes "PAHNAPLSIIGYIR"
        
        Approach:
        - Mathematical simulation based on pattern recognition
        - For each row 'r', calculate the indices of characters that belong to it
        - Characters in top/bottom rows follow a simple arithmetic progression (step = 2*(numRows-1))
        - Characters in middle rows have two components per cycle:
            1. The character at the main index (from the arithmetic progression)
            2. The character in the middle of the zigzag V-shape
        - The formula 'i + increment - 2*r' calculates the index of the middle character
          for rows other than the first and last.
        
        Time Complexity: O(N) where N is the length of the string 's'.
                         We visit each character in the string exactly once.
        Space Complexity: O(1) if we don't count the output string 'res' as extra space.
                          The algorithm uses only a constant amount of extra variables.
        
        Args:
            s: The input string to be converted.
            numRows: The number of rows for the zigzag pattern.
            
        Returns:
            The converted string read line by line from the zigzag pattern.
        """
        if numRows == 1:
            # If only one row, the zigzag is just the original string
            return s

        res = "" # Result string to be built

        for r in range(numRows): # Iterate through each row
            # The fundamental increment for the zigzag cycle
            increment = 2 * (numRows - 1)

            # Iterate through characters in the current row 'r'
            # Start at index 'r', jump by 'increment'
            for i in range(r, len(s), increment):
                res += s[i] # Add the primary character for this row

                # Handle middle rows (not the top or bottom row)
                # These rows have an additional character from the diagonal part of the zigzag
                if r > 0 and r < numRows - 1:
                    # Calculate the index of the middle character in the V-shape
                    # increment is the full cycle length (2*(numRows-1))
                    # 2*r is the offset from the full cycle for the middle character
                    mid_char_index = i + increment - 2 * r
                    
                    # Check if the calculated index is within the string bounds
                    if mid_char_index < len(s):
                        res += s[mid_char_index] # Add the middle character

        return res

def run_zigzag_conversion_test(s, numRows, expected, test_name):
    """
    Tests the convert function.
    
    Args:
        s: Input string to be converted
        numRows: Number of rows for the zigzag pattern
        expected: Expected converted string
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.convert(s, numRows)
    
    print(f"{test_name}:")
    print(f"  Input: s='{s}', numRows={numRows}")
    print(f"  Expected: '{expected}'")
    print(f"  Got:      '{result}'")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_zigzag_conversion_test("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR", "Example 1: Standard zigzag")
run_zigzag_conversion_test("PAYPALISHIRING", 4, "PINALSIGYAHRPI", "Example 2: More rows")
run_zigzag_conversion_test("A", 1, "A", "Edge case: Single character, one row")
run_zigzag_conversion_test("AB", 1, "AB", "Edge case: Two characters, one row")
run_zigzag_conversion_test("ABC", 1, "ABC", "Edge case: Three characters, one row")
run_zigzag_conversion_test("AB", 2, "AB", "Edge case: Two characters, two rows")
run_zigzag_conversion_test("ABC", 2, "ACB", "Edge case: Three characters, two rows")
run_zigzag_conversion_test("ABCD", 2, "ACBD", "Edge case: Four characters, two rows")
run_zigzag_conversion_test("ABCDEF", 3, "AEBDFC", "Edge case: Six characters, three rows")
run_zigzag_conversion_test("", 3, "", "Edge case: Empty string")
run_zigzag_conversion_test("A", 5, "A", "Edge case: Single char, more rows than chars")
