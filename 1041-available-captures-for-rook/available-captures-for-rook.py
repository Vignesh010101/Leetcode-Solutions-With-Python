class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook = None
        while rook is None:
            for i in range(8):
                for j in range(8):
                    if board[i][j] == 'R':
                        rook = (i, j)
                        break
        
        available_captures = 0
        for i in range(rook[0] - 1, -1, -1):
            if board[i][rook[1]] == 'p':
                available_captures += 1
                break
            elif board[i][rook[1]] == 'B':
                break
        for i in range(rook[0] + 1, 8):
            if board[i][rook[1]] == 'p':
                available_captures += 1
                break
            elif board[i][rook[1]] == 'B':
                break
        for j in range(rook[1] - 1, -1, -1):
            if board[rook[0]][j] == 'p':
                available_captures += 1
                break
            elif board[rook[0]][j] == 'B':
                break
        for j in range(rook[1] + 1, 8):
            if board[rook[0]][j] == 'p':
                available_captures += 1
                break
            elif board[rook[0]][j] == 'B':
                break
        return available_captures