class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # Push current string and number to stack
                stack.append(current_str)
                stack.append(current_num)
                # Reset for new encoded section
                current_str = ""
                current_num = 0
            elif char == ']':
                # Pop number and previous string
                num = stack.pop()
                prev_str = stack.pop()
                # Repeat current string and append to previous
                current_str = prev_str + num * current_str
            else:
                # Regular character, add to current string
                current_str += char
        
        return current_str