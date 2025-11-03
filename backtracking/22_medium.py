from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for n pairs.
        
        Problem Understanding:
        - Given n pairs of parentheses
        - Generate all combinations of well-formed parentheses
        - A well-formed parentheses string has equal number of open and close
        - At no point should closing parentheses exceed opening ones
        
        Approach:
        - Use backtracking to build valid combinations
        - Track count of open and close parentheses used
        - Add open parenthesis if count < n
        - Add close parenthesis if count < open count
        - When string length equals 2*n, add to result
        
        Time Complexity: O(4^n / sqrt(n)) - related to Catalan numbers
        Space Complexity: O(4^n / sqrt(n)) for the result (excluding recursion stack)
        
        Args:
            n: Number of pairs of parentheses
            
        Returns:
            List of all valid parentheses combinations
        """
        result = []
        
        def backtrack(current_string, open_count, close_count):
            # Base case: if current string has length 2*n, we have a valid combination
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Add open parenthesis if we haven't used all n open parentheses
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
            
            # Add close parenthesis if it won't make the string invalid
            # (i.e., close_count < open_count)
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)
        return result

def run_generate_parentheses_test(n, expected, test_name):
    """
    Tests the generateParenthesis function.
    
    Args:
        n: Number of pairs of parentheses
        expected: Expected list of valid parentheses combinations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.generateParenthesis(n)
    
    # Convert to sets for order-independent comparison
    result_set = set(result)
    expected_set = set(expected)
    
    print(f"{test_name}:")
    print(f"  Input: n = {n}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print(f"  Count: Expected {len(expected)}, Got {len(result)}")
    print()

# Run test cases
run_generate_parentheses_test(3, ["((()))","(()())","(())()","()(())","()()()"], "Example 1: n=3 -> 5 valid combinations")
run_generate_parentheses_test(1, ["()"], "Example 2: n=1 -> 1 valid combination")
run_generate_parentheses_test(2, ["(())", "()()"], "Edge case: n=2 -> 2 valid combinations")
run_generate_parentheses_test(4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"], "Edge case: n=4 -> 14 valid combinations")
run_generate_parentheses_test(0, [""], "Edge case: n=0 -> [\"\"]")
run_generate_parentheses_test(5, [], "Edge case: n=5 -> 42 valid combinations")