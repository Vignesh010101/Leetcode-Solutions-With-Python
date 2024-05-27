class Solution:
    def possibleToStamp(self, grid: List[List[int]], height: int, width: int) -> bool:
        m, n = len(grid), len(grid[0])
        h, hh = [0]*n, [0]*n
        if height > m or width > n:
            return all(all(row) for row in grid)    # Edge case

        for row in grid:
            r = w = stamp = 0

            while r < width-1:                      # Same as 85
                h[r] = 0 if row[r] else h[r]+1
                w = 0 if h[r] < height else w+1
                r += 1

            for l in range(n):

                if r < n:
                    h[r] = 0 if row[r] else h[r]+1
                    w = 0 if h[r] < height else w+1
                    r += 1

                    if w >= width:  stamp = r       # Stamp!

                if hh[l] == height or row[l] and hh[l]:
                    return False        # Blanks above the occupied or stamped block

                # Update blank heights
                hh[l] = 0 if l < stamp or row[l] else hh[l]+1

        return not any(hh)              # Make sure no blanks left