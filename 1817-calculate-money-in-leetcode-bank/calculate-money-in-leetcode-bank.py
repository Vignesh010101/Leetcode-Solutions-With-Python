class Solution:
    def totalMoney(self, n: int) -> int:
        res=0
        i=1
        j=0
        count=1
        while j<n:
            
            res+=i
            if i==7+count-1:
                count+=1
                i=count
            else:
                i+=1
            j+=1
        
            
            
        
        return(res)
        