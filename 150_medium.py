from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        
        for token in tokens:
            if token in operators:
                # Fix: right operand popped FIRST, left operand popped SECOND
                right = int(stack.pop())
                left = int(stack.pop())
                
                if token == "+":
                    result = left + right
                elif token == "-":
                    result = left - right
                elif token == "*":
                    result = left * right
                elif token == "/":
                    # Fix: Integer division with truncation toward zero
                    result = int(left / right)  # Use int() to truncate toward zero
                
                stack.append(result)
            else:
                stack.append(token)
        
        return int(stack.pop())

if __name__ == "__main__":
    sol = Solution()
    # print(sol.evalRPN(["2","1","+","3","*"]))
    print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))