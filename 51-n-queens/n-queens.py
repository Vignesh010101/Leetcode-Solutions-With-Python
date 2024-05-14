class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []

        def bt(r):
            if r == n:
                result.append(op[:])
            
            for c in range(n):
                if c in col or r+c in dig or r-c in adig:
                    continue
                col.add(c)
                dig.add(r+c)
                adig.add(r-c)
                op.append('.'*c+'Q'+'.'*(n-c-1))
                bt(r+1)
                col.remove(c)
                dig.remove(r+c)
                adig.remove(r-c)
                op.pop()

        col, dig, adig, op, result = set(), set(), set(), [], []
        bt(0)

        return result