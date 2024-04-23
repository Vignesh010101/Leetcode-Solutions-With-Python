class Solution:
    def decodeString(self, s: str) -> str:
        # Initialize the stack and the current string
        stack = []
        curr_str = ""
        # Initialize the current number to 0
        curr_num = 0
        
        # Iterate through each character of the string
        for c in s:
            # If the character is a digit, update the current number
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            # If the character is an opening bracket, push the current number and current string onto the stack
            elif c == "[":
                stack.append(curr_num)
                stack.append(curr_str)
                # Reset the current number and current string
                curr_num = 0
                curr_str = ""
            # If the character is a closing bracket, repeat the popped characters and push the result back onto the stack
            elif c == "]":
                prev_str = stack.pop()
                prev_num = stack.pop()
                curr_str = prev_str + curr_str * prev_num
            # If the character is a letter, append it to the current string
            else:
                curr_str += c
        
        # Pop any remaining characters from the stack and concatenate them to the final result
        while stack:
            curr_str = stack.pop() + curr_str
        
        return curr_str