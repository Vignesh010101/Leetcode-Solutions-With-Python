from math import comb
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        modulo = 10**9+7
        ingoing = defaultdict(set)
        outgoing = defaultdict(set)
        for i in range(1,len(prevRoom)):
            ingoing[i].add(prevRoom[i])
            outgoing[prevRoom[i]].add(i)
        ans = [1]
        def r(i):
            if len(outgoing[i]) == 0:
                return 1 # just self
            nodes_in_tree = 0
            for v in outgoing[i]:
                cn = r(v)
                if nodes_in_tree != 0:
                    ans[0] *= comb(nodes_in_tree+cn,cn)
                    ans[0] %= modulo
                nodes_in_tree += cn
            
            return nodes_in_tree + 1
        
        r(0)
                
        return ans[0] % modulo