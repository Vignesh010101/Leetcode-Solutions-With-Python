class Solution:
    def nz(self, num):
        return not str(num).count('0')
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if self.nz(i) and self.nz(n-i):
                return [i, n-i]