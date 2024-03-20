class Solution:
    def hammingWeight(self, n: int) -> int:
        rslt=0

        for i in range(32):
            if (n>>i)&1:
                rslt+=1
        
        return rslt