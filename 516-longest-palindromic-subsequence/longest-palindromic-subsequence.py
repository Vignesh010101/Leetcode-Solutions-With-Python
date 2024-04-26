class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [0] * n
        prev[n-1] = 1
        for i in range(n-2, -1, -1):
            curr = [0] * n
            curr[i] = 1
            for j in range(i+1, n):
                x = 0
                if s[i] == s[j]:
                    x = prev[j-1] + 2
                y = max(prev[j], curr[j-1])
                curr[j] = max(x, y)
            prev = curr
        return prev[-1]