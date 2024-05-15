class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        '''
            Solves a given recurrence relation
            @params dp: the nth sum per ith equation
            @params coeff: coefficients for the ith equation
        '''
        def solve_rel(dp, coeff):
            for _ in range(n - 1):
                for i in range(len(dp)):
                    tmp = 0
                    for j, c in enumerate(coeff[i]):
                        # If j >= i we must add the second last
                        #value appended, we already updated that dp.
                        tmp += c*dp[j][-1 if j >= i else -2]
                    dp[i].append(tmp)

            return sum(e[-1] for e in dp) % 1000000007


        if m == 1:
            return solve_rel([[3]], [[2]])
        if m == 2:
            return solve_rel([[6]], [[3]])
        elif m == 3:
            return solve_rel([[6], [6]], [[3,2], [2,2]])
        elif m == 4:
            return solve_rel(
                [[6], [6], [6], [6]], 
                [[3,1,2,2], [1,2,1,1], [2,1,2,2], [2,1,2,2]])
        else:
            return solve_rel(
                [[6], [6], [6], [6], [6], [6], [6], [6]],
                [
                    [2,1,1,1,2,2,1,1], 
                    [1,2,1,1,0,0,1,0], 
                    [1,1,2,1,1,1,1,1], 
                    [1,1,1,2,2,2,1,1], 
                    [2,0,1,2,3,2,1,2], 
                    [2,0,1,2,2,2,1,2], 
                    [1,1,1,1,1,1,2,1], 
                    [1,0,1,1,2,2,1,2]
                ])