class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        stp=0
        while num>0:
            if num%2==0:
                num=num//2
                stp+=1
            else:
                num-=1
                stp+=1
        return stp

        