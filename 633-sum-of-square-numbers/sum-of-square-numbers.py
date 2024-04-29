class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=int(c**(1/2))
        while i<=j:
            m=i*i+j*j
            if m==c:
                return True
            elif m>c:
                j-=1
            else:i+=1
        return False