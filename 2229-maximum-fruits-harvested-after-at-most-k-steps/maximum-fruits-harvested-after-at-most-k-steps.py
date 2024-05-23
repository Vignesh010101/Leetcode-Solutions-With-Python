class Solution:
    def maxTotalFruits(self, fruits, start, k):
        def dfs(i,j):
            return fruits[j][0]-fruits[i][0]+min(abs(start-fruits[i][0]),abs(start-fruits[j][0]))

        ans = [0]

        for i,j in fruits:
            ans.append(ans[-1]+j)

        j, max_val, n = 0, 0, len(fruits)

        for i in range(n):
            j = max(i,j)

            while j < n and dfs(i,j) <= k:
                j += 1

            max_val = max(max_val,ans[j]-ans[i])

        return max_val