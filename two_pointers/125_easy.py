class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Checks if a string is a palindrome after converting to lowercase and removing non-alphanumeric characters.
        
        Problem Understanding:
        - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
          and removing all non-alphanumeric characters, it reads the same forward and backward
        - Alphanumeric characters include letters and numbers
        
        Approach:
        - Use two pointers from both ends of the string
        - Skip non-alphanumeric characters
        - Compare characters at both pointers (case-insensitive)
        - Move pointers inward if characters match, return False if they don't
        
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            s: Input string to check
            
        Returns:
            True if the string is a palindrome, False otherwise
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
            
            # Move pointers inward
            left += 1
            right -= 1
        
        return True

def run_palindrome_test(s, expected, test_name):
    """
    Tests the isPalindrome function.
    
    Args:
        s: Input string to check
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.isPalindrome(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_palindrome_test("A man, a plan, a canal: Panama", True, "Example 1: 'A man, a plan, a canal: Panama' -> True")
run_palindrome_test("race a car", False, "Example 2: 'race a car' -> False")
run_palindrome_test(" ", True, "Example 3: ' ' -> True (single space)")
run_palindrome_test("a", True, "Edge case: 'a' -> True")
run_palindrome_test("ab", False, "Edge case: 'ab' -> False")
run_palindrome_test("aba", True, "Edge case: 'aba' -> True")
run_palindrome_test("Aa", True, "Edge case: 'Aa' -> True (case insensitive)")
run_palindrome_test("Madam", True, "Edge case: 'Madam' -> True")
run_palindrome_test("No 'x' in Nixon", True, "Edge case: 'No 'x' in Nixon' -> True")
run_palindrome_test("Mr. Owl ate my metal worm", True, "Edge case: 'Mr. Owl ate my metal worm' -> True")
run_palindrome_test("12321", True, "Edge case: '12321' -> True (numeric palindrome)")
run_palindrome_test("12345", False, "Edge case: '12345' -> False")
run_palindrome_test("", True, "Edge case: Empty string -> True")
run_palindrome_test("!@#$%", True, "Edge case: '!@#$%' -> True (no alphanumeric)")
run_palindrome_test("a1a", True, "Edge case: 'a1a' -> True (alphanumeric palindrome)")