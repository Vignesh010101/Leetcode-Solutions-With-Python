class UnionFind:

    def __init__(self, n: int):
        self.root = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        if self.root[x] != x: self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootx, rooty = self.find(x), self.find(y)
        if rootx == rooty: return
        if self.rank[rootx] > self.rank[rooty]: self.root[rooty] = rootx
        elif self.rank[rootx] < self.rank[rooty]: self.root[rootx] = rooty
        else:
            self.root[rooty] = rootx
            self.rank[rootx] += 1

    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        def get_prime_factors(n: int) -> List[int]:
            s = set()
            while n % 2 == 0:
                s.add(2)
                n //= 2
            
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    s.add(i)
                    n //= i
            if n > 2: s.add(n)
            return list(s)

        primes = collections.defaultdict(int)
        uf = UnionFind(len(nums))
        for i, num in enumerate(nums):
            prime = get_prime_factors(num)
            for p in prime:
                if p in primes: uf.union(primes[p], i)
                primes[p] = i
        
        for i, (_, (_, j)) in enumerate(zip(nums, sorted([(num, i) for i, num in enumerate(nums)]))):
            if not uf.is_connected(i, j): return False
        
        return True