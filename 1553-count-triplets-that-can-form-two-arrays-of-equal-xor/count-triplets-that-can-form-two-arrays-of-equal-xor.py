class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        v=len(arr)
        prefix=[0] * (v+1)

        for i in range(v):
            prefix[i+1]=prefix[i] ^ arr[i]

        count=0
        for i in range(v):
            for j in range(i+1,v):
                if prefix[i]==prefix[j+1]:
                    count+=(j-i)

        return count