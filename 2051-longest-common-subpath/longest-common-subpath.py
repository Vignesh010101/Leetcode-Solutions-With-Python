class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:

        def pivot(n):

            k = pow(base, n-1, mod)
            store = defaultdict(set)

            #Rolling hash
            for j, arr in enumerate(paths):
                arr = [item + 1 for item in arr]
                val = sum(arr[i] * pow(base, n-i-1, mod) for i in range(n)) % mod
                store[val].add(j)
                for i in range(n, len(arr)):
                    val -= arr[i-n] * k
                    val *= base
                    val += arr[i]
                    val %= mod
                    store[val].add(j)

            return max(len(item) for item in store.values()) >= m

        mod = (10 ** 9 + 7) ** 2
        base = 100003
        m = len(paths)

        low = 0
        high = min(len(arr) for arr in paths) + 1

        #Binary search
        while low + 1 < high:
            mid = (low + high) // 2
            if pivot(mid):
                low = mid
            else:
                high = mid

        return low