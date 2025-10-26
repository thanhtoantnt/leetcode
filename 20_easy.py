class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []

        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if stack == []:
                    return False

                matched_char = stack.pop()
                if char == "]" and matched_char != "[":
                    return False

                if char == "}" and matched_char != "{":
                    return False

                if char == ")" and matched_char != "(":
                    return False     
                
        return stack == []

class SolutionOpt:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping.values():  # Open bracket
                stack.append(char)
            else:  # Close bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
                
        return not stack