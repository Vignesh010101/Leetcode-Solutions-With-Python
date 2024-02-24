class Solution:
    def climbStairs(self, n: int) -> int:
        pr1=1
        pr2=1

        for _ in range(2,n+1):
            pr3=pr1+pr2
            pr2,pr1=pr1,pr3
        
        return pr1
