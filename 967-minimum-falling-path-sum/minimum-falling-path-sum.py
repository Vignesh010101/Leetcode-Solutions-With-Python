class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        n = len(m)

        @cache
        def f(i, j):
            if 0 <= j < n:
                if i < n:
                    return m[i][j] + min(f(i+1,j-1), f(i+1,j), f(i+1,j+1))
                else:
                    return 0
            else:
                return inf

        return min(f(0,j) for j in range(n))