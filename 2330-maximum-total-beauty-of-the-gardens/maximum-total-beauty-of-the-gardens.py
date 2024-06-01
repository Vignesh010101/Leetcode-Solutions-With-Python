class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = sorted(min(target, x) for x in flowers)
        prefix = [0]
        ii = -1 
        for i in range(len(flowers)): 
            if flowers[i] < target: ii = i 
            if i: prefix.append(prefix[-1] + (flowers[i]-flowers[i-1])*i)
        ans = 0 
        for k in range(len(flowers)+1): 
            if k: newFlowers -= target - flowers[-k]
            if newFlowers >= 0: 
                while 0 <= ii and (ii+k >= len(flowers) or prefix[ii] > newFlowers): ii -= 1
                if 0 <= ii: kk = min(target-1, flowers[ii] + (newFlowers - prefix[ii])//(ii+1))
                else: kk = 0 
                ans = max(ans, k*full + kk*partial)
        return ans 