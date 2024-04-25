class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        ia = list(map(lambda x:ord(x) - ord('a'), p))

        runs = {i: 0 for i in range(26)}
        st, r, la = ia[0], 1, ia[0]
        def proc():
            nonlocal st, r, la
            nonlocal runs
            for i in range(27):
                if runs[st]<r:
                    runs[st]=r
                st, r = (st+1)%26, r - 1
                if r<=0:
                    break


        for i in ia[1:]:
            if i == la + 1 or la == 25 and i == 0:
                st, r, la = st, r + 1, i
            else:
                proc()
                st, r, la = i, 1, i
        proc()

        ret = 0
        for i in runs.values():
            ret += i

        return ret

