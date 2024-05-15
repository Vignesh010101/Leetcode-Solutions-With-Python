class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        minR,maxR=999999,-122
        players=''
        for i in range(1,n+1):
            players+=chr(i+65)
        fp=chr(firstPlayer+65)
        sp=chr(secondPlayer+65)

        @cache
        def dfs(s,num_round,winners):
            nonlocal maxR, minR
            if len(s)==0:
                dfs("".join(sorted(winners)),num_round+1,'')
                return
            if len(s)==1:
                winners+=s[0]
                dfs("".join(sorted(winners)),num_round+1,'')
                return
            if s[0]==fp and s[-1]==sp:
                
                maxR=max(maxR,num_round)
                minR=min(minR,num_round)
                return
            elif s[0]==fp or s[0]==sp:
                winners+=s[0]
                s=s[1:-1]
                dfs(s,num_round,winners)
            elif s[-1]==fp or s[-1]==sp:
                winners+=s[-1]
                s=s[1:-1]
                dfs(s,num_round,winners)
            else:
                l,r=s[0],s[-1]
                dfs(s[1:-1],num_round,winners+l)
                dfs(s[1:-1],num_round,winners+r)
            return
        
        dfs(players, 1, '')
        return [minR,maxR]


            