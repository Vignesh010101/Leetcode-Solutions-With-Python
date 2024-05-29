class Solution:
    def numSteps(self, s: str) -> int:
        value=int(s, 2)
        count=0
        while value>1:
            if value % 2==0:
                value //= 2
            else:
                value+=1
            count+=1
        return count