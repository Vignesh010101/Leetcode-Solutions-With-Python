class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        Mod = 10**9+7  # Define the modulus
        n, m = len(grid), len(grid[0])  # Get the size of the grid
        row = [-1 for _ in range(m)]  # Initialize the visited state of each row as -1
        visited = [row[:] for _ in range(n)]  # Initialize the visited state of the entire grid as -1

        def dfs(i, j):
            if visited[i][j] != -1:  # If the position has been visited before, directly return the visited result
                return visited[i][j]
            result = 1  # Initial result is 1, representing the number of paths from the current position to the destination
            adj = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]  # Define the four directions for adjacent positions
            for a, b in adj:
                if 0 <= a < n and 0 <= b < m:  # Make sure the adjacent position is within the grid
                    if grid[a][b] > grid[i][j]:  # If the height of the adjacent position is greater than the current position, continue exploring in that direction
                        result = (result + dfs(a, b)) % Mod  # Update the result and take the modulus
            visited[i][j] = result  # Save the result to the visited state to avoid duplicate calculations
            return result

        result = 0  # Initial result is 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == -1:  # If the position has not been visited yet, perform depth-first search
                    visited[i][j] = dfs(i, j)  # Update the visited result of that position
                result = (result + visited[i][j]) % Mod  # Add the visited result of that position to the final result and take the modulus

        # Uncomment the following line to print the visited state matrix
        # print(visited)

        return result  # Return the final result