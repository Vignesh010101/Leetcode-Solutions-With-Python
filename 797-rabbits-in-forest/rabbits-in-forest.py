class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #total rabbits
        m = defaultdict(int)
        mincnt = 0 

        for i in answers:
            m[i]+=1

        for x,y in zip(m.keys(),m.values()) :
                mincnt = mincnt +ceil(y/(x+1))*(x+1)
        
        return mincnt
        # 3 3 3 3 3 3 