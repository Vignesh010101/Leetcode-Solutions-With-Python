class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        factors = []
        for x in range(1, int(sqrt(k))+1):
            if k % x == 0: factors.append(x)
        ans = 0 
        freq = Counter()
        for x in nums: 
            x = gcd(x, k)
            ans += freq[k//x]
            for f in factors: 
                if x % f == 0 and f <= x//f: 
                    freq[f] += 1
                    if f < x//f: freq[x//f] += 1
        return ans 