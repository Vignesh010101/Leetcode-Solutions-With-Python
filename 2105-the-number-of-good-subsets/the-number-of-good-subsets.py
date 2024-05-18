class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        '''
        1 <= nums[i] <= 30


        bitmask?
        
        distinct prime numbers
        '''
        MOD = 10 ** 9 + 7
        primes = set({2, 3, 5, 7, 11, 13, 17, 19, 23, 29})
        mask = defaultdict(int)
        
        for index, num in enumerate([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]):
            mask[num] = 1 << index
            
        
        mask_of_num = defaultdict(int)
        
        options = []
        
        for n in nums:
            start = 0
            
            check = True
            for p in primes:
    
                
                if n % (p ** 2) == 0:  
                    check = False
                    break
                        
                if n % p == 0:
                    start |= mask[p]
                    
            if check:
                mask_of_num[n] = start
                options.append(n)
                
            
        N = len(options)
        c = Counter(options)

        @cache
        def calc(x, m):
            if x == 31:
                return int(m != 0)

            best = calc(x + 1, m)

            if c[x]:
                if x == 1:
                    # choose to include or not include c[s] 1's
                    best *= 2 ** c[x]
                
                elif m & mask_of_num[x] == 0:
                    # include 1 of the x c[x] times
                    best += c[x] * calc(x + 1, m | mask_of_num[x])

            return best % MOD
        
        return calc(1, 0) % MOD