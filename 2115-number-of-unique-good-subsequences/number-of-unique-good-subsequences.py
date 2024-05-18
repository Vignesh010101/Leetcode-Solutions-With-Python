class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        mod = 10**9 + 7
        dp = [[0, 0] for _ in range(2)]  # dp[i][j] represents count of subsequences ending at index i with last element j (0 or 1)
        n = len(binary)
        
        for ch in binary:
            if ch == '0':
                # For a '0', we have two cases:
                # 1. Extend the subsequences ending with '0' by one more '0'.
                # 2. Extend the subsequences ending with '1' by appending this '0' to form new subsequences.
                dp[0][0] = 1
                dp[1][0] = (dp[1][0] + dp[1][1]) % mod
            else:
                # For a '1', we have one case:
                # Extend the subsequences ending with '0' or '1' by appending this '1' to form new subsequences.
                dp[1][1] = (dp[1][0] + dp[1][1] + 1) % mod
        
        # The answer is the sum of counts of subsequences ending with '0' and '1',
        # considering all the possibilities.
        result = (dp[0][0] + dp[0][1] + dp[1][0] + dp[1][1]) % mod
        return result

# Create an instance of the Solution class
sol = Solution()