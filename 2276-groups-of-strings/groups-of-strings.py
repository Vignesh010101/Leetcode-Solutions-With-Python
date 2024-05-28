class UnionFind: 
    def __init__(self, n): 
        self.parent = list(range(n))
        self.rank = [1] * n 
        
    def find(self, p): 
        if p != self.parent[p]: 
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]
    
    def union(self, p, q): 
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt
        self.parent[prt] = self.parent[qrt]
        self.rank[qrt] += self.rank[prt]
        return True 


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n = len(words)
        uf = UnionFind(n)
        seen = {}
        for i, word in enumerate(words): 
            m = reduce(or_, (1<<ord(ch)-97 for ch in word))
            if m in seen: uf.union(i, seen[m])
            for k in range(26): 
                if m ^ 1<<k in seen: uf.union(i, seen[m ^ 1<<k])
                if m & 1<<k: 
                    mm = m ^ 1<<k ^ 1<<26
                    if mm in seen: uf.union(i, seen[mm])
                    seen[mm] = i
            seen[m] = i 
        freq = Counter(uf.find(i) for i in range(n))
        return [len(freq), max(freq.values())]