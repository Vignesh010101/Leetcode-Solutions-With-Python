class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        m, n = Counter(s), len(s)
        stack = []
        cnt = m[letter]
        for i, c in enumerate(s):
            while stack and stack[-1] > c and len(stack) + n - i - 1 >= k and (stack[-1] !=letter or cnt > repetition):
                top_c = stack[-1]
                if top_c == letter:
                    repetition += 1
                stack.pop()
            
            if len(stack) < k:
                if c == letter:
                    stack.append(c)
                    repetition -= 1
                elif k - len(stack) > repetition:
                    stack.append(c)
            if c== letter:
                cnt = cnt - 1
        return "".join(stack)

            
            
        