class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        wins = [{(0, 0), (0, 1), (0, 2)}, {(1, 0), (1, 1), (1, 2)}, {(2, 0), (2, 1), (2, 2)}, {(0, 0), (1, 0), (2, 0)}, {(0, 1), (1, 1), (2, 1)}, {(0, 2), (1, 2), (2, 2)}, {(0, 0), (1, 1), (2, 2)}, {(1, 1), (0, 2), (2, 0)}]
        move_A = []
        move_B = []
        for i in range(0, len(moves), 2):
            move_A.append(moves[i])
            if i + 1 < len(moves):
                move_B.append(moves[i + 1])
        move_A = set(tuple(sublist) for sublist in move_A)
        move_B = set(tuple(sublist) for sublist in move_B)
        for win_set in wins:
            if win_set <= move_A:
                return "A"
            if win_set <= move_B:
                return "B"
            continue
        if len(moves) == 9:
            return "Draw"
        else:
            return "Pending"
        