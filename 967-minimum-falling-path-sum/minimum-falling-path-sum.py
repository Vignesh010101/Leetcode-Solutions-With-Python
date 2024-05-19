class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        return min(reduce(lambda a,r:[q+min(a[max(0,j-1):j+2]) for j,q in enumerate(r)],m))