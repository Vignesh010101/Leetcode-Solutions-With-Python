from heapq import heappush,heappop
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        heap=[]
        arr=[]
        for i in d:
            heappush(heap,[d[i],-i])
        while(heap):
            m,n=heappop(heap)
            for i in range(m):
                arr.append(n*(-1))
        return(arr)
                
            