from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Returns all possible letter combinations that the number could represent.
        
        Problem Understanding:
        - Given a string containing digits from 2-9
        - Return all possible letter combinations based on phone keypad mapping
        - Each digit maps to certain letters (like on traditional phone keypad)
        
        Approach:
        - Use backtracking to build combinations incrementally
        - Create mapping from digits to letters
        - At each position in the input digits, try all possible letters for that digit
        - Continue recursively until combination length equals digits length
        - Backtrack by removing the last added letter
        
        Time Complexity: O(3^N * 4^M) where N is number of digits mapping to 3 letters, 
                         M is number of digits mapping to 4 letters
        Space Complexity: O(3^N * 4^M) for the result (excluding recursion stack)
        
        Args:
            digits: String of digits from 2-9
            
        Returns:
            List of all possible letter combinations
        """
        if not digits:
            return []
        
        # Mapping of digits to letters
        digit_to_letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index, current_combination):
            # Base case: if we've processed all digits, add combination to result
            if index == len(digits):
                result.append(current_combination)
                return
            
            # Get letters for current digit
            current_digit = digits[index]
            letters = digit_to_letters[current_digit]
            
            # Try each letter for current digit
            for letter in letters:
                # Add letter to combination and continue recursively
                backtrack(index + 1, current_combination + letter)
        
        backtrack(0, "")
        return result

def run_letter_combinations_test(digits, expected, test_name):
    """
    Tests the letterCombinations function.
    
    Args:
        digits: Input string of digits from 2-9
        expected: Expected list of letter combinations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.letterCombinations(digits)
    
    # Convert to sets for order-independent comparison
    result_set = set(result)
    expected_set = set(expected)
    
    print(f"{test_name}:")
    print(f"  Input: '{digits}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_letter_combinations_test("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"], "Example 1: '23' -> 9 combinations")
run_letter_combinations_test("", [], "Example 2: '' -> []")
run_letter_combinations_test("2", ["a","b","c"], "Example 3: '2' -> ['a','b','c']")
run_letter_combinations_test("7", ["p","q","r","s"], "Edge case: '7' -> ['p','q','r','s']")
run_letter_combinations_test("234", [], "Edge case: '234' -> 27 combinations")
run_letter_combinations_test("9", ["w","x","y","z"], "Edge case: '9' -> ['w','x','y','z']")
run_letter_combinations_test("27", ["ap","aq","ar","as","bp","bq","br","bs","cp","cq","cr","cs"], "Edge case: '27' -> 12 combinations")
run_letter_combinations_test("78", ["pt","pu","pv","qt","qu","qv","rt","ru","rv","st","su","sv"], "Edge case: '78' -> 12 combinations")
run_letter_combinations_test("2345", [], "Edge case: '2345' -> 81 combinations")
run_letter_combinations_test("789", [], "Edge case: '789' -> 64 combinations")