class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        ans, n = 0, len(statements)
        for person in itertools.product([0, 1], repeat=n): # use itertools to create a list only contains 0 or 1
            valid = True                                   # initially, we think the `person` list is valid
            for i in range(n):
                if not person[i]: continue                 # only `good` person's statement can lead to a contradiction, we don't care what `bad` person says
                for j in range(n):
                    if statements[i][j] == 2: continue     # ignore is no statement was made
                    if statements[i][j] != person[j]:      # if there is a contradiction, then valid = False
                        valid = False
                        break                              # optimization: break the loop when not valid
                if not valid:                              # optimization: break the loop when not valid
                    break        
            if valid: 
                ans = max(ans, sum(person))                # count sum only when valid == True
        return ans