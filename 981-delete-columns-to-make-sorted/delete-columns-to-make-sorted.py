class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs[0])
        ct=0
        lst=["" for _ in range(n)]
        for i in range(len(strs)):
            for j in range(n):
                if lst[j]=="":
                    lst[j]=strs[i][j]
                elif lst[j]==-1:
                    continue
                elif ord(lst[j])>ord(strs[i][j]):
                    lst[j]=-1
                    ct+=1
                else:
                    lst[j]=strs[i][j]
        return ct