mod=1337
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res=1
        v=len(b)-1
        p=a
        while v>=0:
            res=(res*pow(p,b[v],mod))%mod
            p=pow(p,10,mod)
            v-=1
        return res
