class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        list1=[]
        x=sorted(set(arr))
        dict1={}
        for i in range(len(x)):
            dict1[x[i]]=i+1
        for j in arr:
            y=dict1[j]
            list1.append(y)
        return list1