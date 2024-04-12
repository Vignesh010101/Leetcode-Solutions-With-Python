class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=-1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>n:
                n,arr[i]=arr[i],n
            else:
                arr[i]=n
        return arr