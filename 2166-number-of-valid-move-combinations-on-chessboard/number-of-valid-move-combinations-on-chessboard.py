class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        n = len(pieces)
        mp = {"bishop": ((-1, -1), (-1, 1), (1, -1), (1, 1)),
              "queen" : ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)), 
              "rook"  : ((-1, 0), (0, -1), (0, 1), (1, 0))}
        
        dirs = [[]] # directions
        for piece in pieces: dirs = [x+[xx] for x in dirs for xx in mp[piece]]
        
        positions = tuple(map(tuple, positions))
        
        def fn(*args): 
            """Return possible moves along given direction."""
            stack = [((1<<n)-1, positions)]
            while stack: 
                mask, pos = stack.pop()
                ans.add(pos)
                m = mask
                while m: 
                    p = []
                    for i in range(n): 
                        if m & (1 << i): 
                            p.append((pos[i][0] + args[i][0], pos[i][1] + args[i][1]))
                            if not (1 <= p[i][0] <= 8 and 1 <= p[i][1] <= 8): break 
                        else: p.append(pos[i])
                    else: 
                        cand = tuple(p)
                        if len(set(cand)) == len(cand) and m: stack.append((m, cand))
                    m = mask & (m-1)

        ans = set()
        for d in dirs: fn(*d)
        return len(ans)