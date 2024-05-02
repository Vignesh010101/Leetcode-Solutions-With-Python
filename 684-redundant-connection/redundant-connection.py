class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def UnionBySize(self, irep, jrep):
        isize = self.size[irep]
        jsize = self.size[jrep]

        if isize < jsize:
            self.parent[irep] = jrep
            self.size[jrep] += self.size[irep]
        else:
            self.parent[jrep] = irep
            self.size[irep] += self.size[jrep]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for (i, j) in edges:
            irep = uf.find(i-1)
            jrep = uf.find(j-1)
            if irep != jrep:
                uf.UnionBySize(irep, jrep)
            else:
                return [i, j]
            