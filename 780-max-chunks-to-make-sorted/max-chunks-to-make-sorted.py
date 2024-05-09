class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunk=0
        max_v=[0]*len(arr)
        max_v[0]=arr[0]

        for i in range(1,len(arr)):
            max_v[i]=max(max_v[i-1],arr[i])

        for i in range(len(arr)):
            if max_v[i]==i:
                chunk+=1

        return chunk