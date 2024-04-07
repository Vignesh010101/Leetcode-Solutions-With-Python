class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(col):
            first = matrix[0][i]
            j = i 
            r = 0
            while j<col and r<row:
                if first != matrix[r][j]:
                    return False
                j += 1
                r += 1
        
        for i in range(1,row):
            first = matrix[i][0]
            j = 0 
            r = i
            while j<col and r<row:
                if first != matrix[r][j]:
                    return False
                j += 1
                r += 1
        return True