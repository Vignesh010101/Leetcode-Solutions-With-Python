class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        result = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        
        def bfs(start_row, start_col):
            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            min_row, min_col, max_row, max_col = start_row, start_col, start_row, start_col
            
            while queue:
                cur_row, cur_col = queue.popleft()
                
                for dr, dc in directions:
                    new_row, new_col = cur_row + dr, cur_col + dc
                    
                    if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and land[new_row][new_col] == 1:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        min_row = min(min_row, new_row)
                        min_col = min(min_col, new_col)
                        max_row = max(max_row, new_row)
                        max_col = max(max_col, new_col)
            
            return [min_row, min_col, max_row, max_col]
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    farmland = bfs(i, j)
                    result.append(farmland)
        
        return result