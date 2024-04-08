class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        top=left=0
        bottom=len(image);right=len(image[0])
        res=[]
        while left<right and top<bottom:
            for i in range(left,right):
                res.append(image[top][i])
            top+=1
        l=[]
        for i in range(0,len(res),right):
            s=res[i:i+right]
            if len(s)==right:
                l.append(s[::-1])
        x=[]
        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j]==0:
                    l[i][j]=1
                else:
                    l[i][j]=0
        return l