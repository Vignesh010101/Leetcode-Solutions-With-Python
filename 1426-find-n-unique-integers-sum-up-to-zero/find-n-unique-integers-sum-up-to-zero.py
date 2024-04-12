class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        mid=n>>1

        for _ in range(mid):
            ans.append(mid)
            ans.append(-mid)
            mid-=1

        if n&1:
            ans.append(0)

        return ans