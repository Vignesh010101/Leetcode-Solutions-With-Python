class Solution:
    def numberOfCombinations(self, num: str) -> int:
        N = len(num)
        m = 1000000007

        lcp = [[0] * (N + 1) for _ in range(N + 1)]
        for i in range(N- 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if num[i] == num[j]:
                    lcp[i][j] = 1 + lcp[i + 1][j + 1]

        dp2 = [[0] * (N) for _ in range(N + 1)]
        for j in range(N):
            dp2[N][j] = 1
        
        for i in range(N - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                # i is the idx, j is the lastIdx from previous solution, check below
                ans = 0
                # form new num at i
                if num[i] != '0':
                    def isGreaterOrEqual(start1, start2, length):
                        cp = lcp[start1][start2]
                        return cp >= length or num[start1 + cp] >= num[start2 + cp]

                    nextIdx = 2 * i - j
                    if nextIdx <= N:
                        if isGreaterOrEqual(i, j, i - j):
                            ans = (ans + dp2[nextIdx][i]) % m
                        else:
                            if nextIdx < N:
                                nextIdx += 1
                                ans = (ans + dp2[nextIdx][i]) % m
                
                # push into the previous
                ans = (ans + dp2[i + 1][j]) % m
                dp2[i][j] = ans
        
        # only one option at the idx = 0, no prev num
        if num[0] != '0':
            dp2[0][0] = dp2[1][0]
        
        return dp2[0][0]
        