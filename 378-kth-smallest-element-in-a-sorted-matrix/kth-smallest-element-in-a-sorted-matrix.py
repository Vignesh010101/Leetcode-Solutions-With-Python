import numpy as np
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        vy=np.array(matrix).flatten()
        vy.sort()
        return vy[k-1]