class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        import copy
        w = copy.deepcopy(score)
        l=[]
        m = 0
        if(len(score)==1):
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i] = 'Gold Medal'
            return w
        elif(len(score)==2):
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i] = 'Gold Medal'
            score.remove(c)    
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i]= 'Silver Medal'
            c = max(score) 
            return w
        else:
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i] = 'Gold Medal'
            score.remove(c)    
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i]= 'Silver Medal'
            score.remove(c)    
            c = max(score)
            for i in range(len(w)):
                if(w[i]==c):
                    w[i]='Bronze Medal'
            score.remove(c)
            u = sorted([i for i in w if type(i)==int],reverse = True)
            for i in range(len(w)):
                if type(w[i])==int:
                    r = u.index(w[i])+4
                    w[i] = str(r)
            return w