from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        # Generate all cells
        all_cells = [[r, c] for r in range(rows) for c in range(cols)]
        
        # Sort cells by Manhattan distance from (rCenter, cCenter)
        all_cells.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        
        # Return sorted cells
        return all_cells