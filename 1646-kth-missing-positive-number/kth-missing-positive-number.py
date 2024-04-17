class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst1=[]
        for i in range(1,2009):
            lst1.append(i)
        for j in arr:
            if j in lst1:
                lst1.remove(j)

        return lst1[k-1]