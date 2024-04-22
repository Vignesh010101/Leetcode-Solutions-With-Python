class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends to a set for O(1) lookup
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        # Initialize BFS
        queue = deque([('0000', 0)])  # (current_combination, moves)
        visited = set('0000')
        
        # BFS loop
        while queue:
            current_combination, moves = queue.popleft()
            
            # Check if we've reached the target
            if current_combination == target:
                return moves
            
            # Generate next possible combinations
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = (
                        current_combination[:i] + str(new_digit) + current_combination[i+1:]
                    )
                    
                    # Check if the new combination is valid and not visited
                    if new_combination not in visited and new_combination not in deadends:
                        visited.add(new_combination)
                        queue.append((new_combination, moves + 1))
        
        # If target is not reachable
        return -1