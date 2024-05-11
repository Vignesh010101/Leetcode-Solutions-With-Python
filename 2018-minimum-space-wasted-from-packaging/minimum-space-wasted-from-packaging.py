from collections import defaultdict
from bisect import bisect_left,bisect_right
class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:

        packages.sort()

        l=len(packages)

        #prefix sum of packages
        pre=[0 for i in range(l)]
        pre[0]=packages[0]

        for i in range(1,l):
            pre[i]+=pre[i-1]+packages[i]

        #print('pre ',pre)

        minn=10000000000

        #for each supplier
        for i in boxes:
            
            flag=False

            #sorting the box of supplier
            i.sort()
            
            #lenght of supplier
            L=len(i)

            #wastage of supplier
            wastage=0

            last=-1

            #for each design of supplier
            for j in i:
                
                ind=bisect_right(packages,j)

                if ind<l:

                    summ=pre[ind]-packages[ind]

                elif ind==l:

                    flag=True
                    summ=pre[ind-1]
                
                tt=0
                if last<0:
                    tt=ind
                else:
                    tt=(ind-last-1)
                    summ-=pre[last]

                wastage+=((tt*j)-(summ))

                last=ind-1

            if flag:
                minn=min(minn,wastage)%1000000007

        if minn>=1000000000:
            return -1
        return minn%1000000007





                
                
            