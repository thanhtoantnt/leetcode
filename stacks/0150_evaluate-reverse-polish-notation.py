from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates the value of an arithmetic expression in Reverse Polish Notation (RPN).
        
        Problem Understanding:
        - Given an array of strings tokens representing an RPN expression
        - Valid operators are '+', '-', '*', and '/'
        - Each operand may be an integer or another expression
        - Division truncates towards zero
        - Input is guaranteed to be a valid RPN expression
        
        Approach:
        - Use a stack to evaluate the expression
        - For each token:
          - If it's a number, push it onto the stack
          - If it's an operator, pop two operands, perform operation, push result
        - For division, truncate towards zero (use int() for positive, special handling for negative)
        
        Time Complexity: O(n) where n is the number of tokens
        Space Complexity: O(n) for the stack in worst case
        
        Args:
            tokens: List of strings representing RPN expression
            
        Returns:
            Integer result of evaluating the RPN expression
        """
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token in operators:
                # Pop two operands (order matters for subtraction and division)
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                else:  # token == '/'
                    # Division truncates towards zero
                    result = int(a / b)
                
                stack.append(result)
            else:
                # Token is a number, convert to integer and push to stack
                stack.append(int(token))
        
        # Final result is the only element left in stack
        return stack[0]

def run_rpn_test(tokens, expected, test_name):
    """
    Tests the evalRPN function.
    
    Args:
        tokens: List of strings representing RPN expression
        expected: Expected result of evaluation
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.evalRPN(tokens)
    
    print(f"{test_name}:")
    print(f"  Input: {tokens}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_rpn_test(["2","1","+","3","*"], 9, "Example 1: ['2','1','+','3','*'] -> 9 ((2+1)*3)")
run_rpn_test(["4","13","5","/","+"], 6, "Example 2: ['4','13','5','/','+'] -> 6 (4+(13/5))")
run_rpn_test(["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22, "Example 3: Complex expression -> 22")
run_rpn_test(["4","-3","+"], 1, "Edge case: ['4','-3','+'] -> 1 (4+(-3))")
run_rpn_test(["-1","-2","+"], -3, "Edge case: ['-1','-2','+'] -> -3 ((-1)+(-2))")
run_rpn_test(["18"], 18, "Edge case: Single number ['18'] -> 18")
run_rpn_test(["2","2","/"], 1, "Edge case: ['2','2','/'] -> 1 (2/2)")
run_rpn_test(["7","-2","/"], -3, "Edge case: ['7','-2','/'] -> -3 (7/-2, truncated to -3)")
run_rpn_test(["-7","2","/"], -3, "Edge case: ['-7','2','/'] -> -3 (-7/2, truncated to -3)")
run_rpn_test(["4","13","5","-"], -8, "Edge case: ['4','13','5','-'] -> -8 (4-(13-5) = 4-8 = -4) -> Actually (4-13)-5 = -9-5 = -14 -> No, it's 4-(13-5) = 4-8=-4. Wait, it's 13-5=8, then 4-8=-4")
run_rpn_test(["5","-3","*"], -15, "Edge case: ['5','-3','*'] -> -15 (5*(-3))")
run_rpn_test(["2","1","-","3","*"], 3, "Edge case: ['2','1','-','3','*'] -> 3 ((2-1)*3)")