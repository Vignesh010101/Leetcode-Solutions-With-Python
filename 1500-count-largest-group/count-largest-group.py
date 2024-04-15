class Solution:
    def countLargestGroup(self, n: int) -> int:
        return max(Counter(Counter(sum(map(int,str(i))) for i in range(1,n+1)).values()).items())[1]