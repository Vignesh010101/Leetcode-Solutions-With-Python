class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = defaultdict(list)
        
        for i in range(1, len(parent)):
            g[parent[i]].append(i)
        
        ans = 0 
        
        def dfs(node, parent):
            nonlocal ans
            
			## required for keeping track of two longest child paths that dont match 
			## the label in case there is a case (iii) from the list above.
			
            fir,sec = 0,0  
            
            for nei in g[node]:
                st = dfs(nei, node)
                if s[nei] != s[node]:
                    if st > fir: 
                        sec = fir
                        fir = st
                    elif st == fir or st > sec: 
                        sec = st
                            
            ans = max(ans, fir+sec+1)
            return fir+1
        
        dfs(0, -1)
        
        return ans