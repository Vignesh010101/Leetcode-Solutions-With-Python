class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific, atlantic = set(), set()
        result = []

        def dfs_explore(r, c, ocean_set, prev_height):
            if (   r < 0 or r >= ROWS 
                or c < 0 or c >= COLS 
                or (r, c) in ocean_set
                or heights[r][c] < prev_height
            ): return
            
            ocean_set.add((r, c))

            for dr, dc in DIRECTIONS:
                dfs_explore(r + dr, c + dc, ocean_set, heights[r][c])
        
        # Water Flow Simulation from North and South borders.
        for col in range(COLS):
            dfs_explore(0, col, pacific, heights[0][col])
            dfs_explore(ROWS - 1, col, atlantic, heights[ROWS - 1][col])

        # Water Flow Simulation from West and East borders.
        for row in range(ROWS):
            dfs_explore(row, 0, pacific, heights[row][0])
            dfs_explore(row, COLS - 1, atlantic, heights[row][COLS - 1])

        # Check if current cell reacheas both Oceans.
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result 