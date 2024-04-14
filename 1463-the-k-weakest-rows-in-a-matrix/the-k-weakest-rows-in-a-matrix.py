class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [(sum(mat[i]),i) for i in range(len(mat))]
        heapq.heapify(arr)
        res = []
        for _ in range(k):
            _,row = heapq.heappop(arr)
            res.append(row)
        return res