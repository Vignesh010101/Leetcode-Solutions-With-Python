class Solution:
    def pivotInteger(self, n: int) -> int:
       y=(n*n+n)//2
       x=int(math.sqrt(y))
       return x if x*x==y else -1 