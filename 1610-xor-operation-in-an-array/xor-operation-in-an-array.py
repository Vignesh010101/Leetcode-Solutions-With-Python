class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda i,j:i^j, [start+2*i for i in range(n)])