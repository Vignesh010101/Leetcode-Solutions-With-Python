class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_count = 0
        right_count = 0
        stack = []

        # Pass 1
        for ch in s:
            if ch == '(':
                left_count += 1
            elif ch == ')':
                right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(ch)

        result = ""

        # Pass 2
        while stack:
            current_char = stack.pop()
            if left_count > right_count and current_char == '(':
                left_count -= 1
            else:
                result += current_char

        # Reverse the result string
        return result[::-1]