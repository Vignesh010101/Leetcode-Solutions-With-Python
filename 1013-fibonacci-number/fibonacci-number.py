class Solution(object):
    memo = {}
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1: return 1
        if n in self.memo:return self.memo[n]
        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result
        return result