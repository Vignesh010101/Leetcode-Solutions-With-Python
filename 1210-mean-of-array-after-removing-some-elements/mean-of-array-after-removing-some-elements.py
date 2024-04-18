class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n=int(0.05*len(arr))
        for i in range(n):
            arr.remove(min(arr))
            arr.remove(max(arr))
        return sum(arr)/len(arr)
