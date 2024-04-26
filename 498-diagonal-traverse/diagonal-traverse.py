class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        R, C = len(mat), len(mat[0])
        
        diagonal_dict = defaultdict(list)
        
        for r in range(R):
            for c in range(C):
                diagonal_dict[r+c].append(mat[r][c])
                
        ans = []
        
        key = 0
        
        while key in diagonal_dict:
            if key%2: #odd
                ans.extend(diagonal_dict[key])
            else: #even
                ans.extend(diagonal_dict[key][::-1])
            
            key+=1
        
        return ans