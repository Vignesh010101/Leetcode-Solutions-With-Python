class Solution:
    def grayCode(self, n: int) -> List[int]:
        rslt=[0]
        for i in range(n):
            for j in reversed(range(len(rslt))):
                rslt.append(rslt[j] | 1 << i)
        
        return rslt