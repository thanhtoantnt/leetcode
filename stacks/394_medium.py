class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decodes an encoded string based on the pattern k[encoded_string].
        
        Problem Understanding:
        - The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
          is repeated exactly k times
        - k is a positive integer
        - Input string is always valid with properly formed brackets
        - Digits are only for repeat numbers k, not part of the encoded string
        
        Approach:
        - Use a stack to handle nested structures
        - Keep track of current number and current string being built
        - When encountering '[', push current string and number to stack, reset
        - When encountering ']', pop from stack and repeat current string that many times
        - When encountering a digit, build the number
        - When encountering a letter, add to current string
        
        Time Complexity: O(maxK * n) where maxK is the maximum value of k and n is the length of the string
        Space Complexity: O(m) where m is the size of the decoded string
        
        Args:
            s: Encoded string
            
        Returns:
            Decoded string
        """
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # Build the number (in case it's multi-digit)
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current string and number to stack
                # Reset for the new bracketed section
                stack.append((current_str, current_num))
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop the previous string and repeat count
                prev_str, repeat_count = stack.pop()
                # Repeat current string and append to previous string
                current_str = prev_str + current_str * repeat_count
            else:  # It's a letter
                # Add to current string being built
                current_str += char
        
        return current_str

def run_decode_string_test(s, expected, test_name):
    """
    Tests the decodeString function.
    
    Args:
        s: Encoded string
        expected: Expected decoded string
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.decodeString(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: '{expected}'")
    print(f"  Got: '{result}'")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_decode_string_test("3[a]2[bc]", "aaabcbc", "Example 1: '3[a]2[bc]' -> 'aaabcbc'")
run_decode_string_test("3[a2[c]]", "accaccacc", "Example 2: '3[a2[c]]' -> 'accaccacc'")
run_decode_string_test("2[abc]3[cd]ef", "abcabccdcdcdef", "Example 3: '2[abc]3[cd]ef' -> 'abcabccdcdcdef'")
run_decode_string_test("abc3[cd]xyz", "abccdccdcdxyz", "Edge case: 'abc3[cd]xyz' -> 'abccdccdcdxyz'")
run_decode_string_test("100[leetcode]", "100 times leetcode", "Edge case: Large repeat count -> 100 times leetcode")
run_decode_string_test("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef", "Edge case: Complex nested structure")
run_decode_string_test("x2[y3[z]]", "xyzzzyzzz", "Edge case: 'x2[y3[z]]' -> 'xyzzzyzzz'")
run_decode_string_test("2[2[ab]]", "abababab", "Edge case: Nested repetition -> 'abababab'")
run_decode_string_test("a", "a", "Edge case: Single character -> 'a'")
run_decode_string_test("", "", "Edge case: Empty string -> ''")
run_decode_string_test("3[a]0[b]2[c]", "aaccc", "Edge case: Zero repeat -> 'aaccc'")
run_decode_string_test("1[a1[b1[c]]]", "abc", "Edge case: 1 repeat -> 'abc'")