class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat[0])
        diagSum = [0,0]
        odd = n%2
        
        for i in range(1):
            for j in range(n):
                if odd and j == (n//2):
                    diagSum[0] += mat[j][j]
                else:
                    diagSum[0] += mat[j][j]
                    diagSum[1] += mat[j][n-1-j]

        return diagSum[0] + diagSum[1]