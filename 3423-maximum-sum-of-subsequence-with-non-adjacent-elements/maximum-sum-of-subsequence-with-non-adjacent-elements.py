inf = -float('inf')
class SegTree:
    def __init__(self, nums):
        n = len(nums)
        # each element: [nn, ny, yn, yy]
        self.ar = [None] * (4*n+1)
        self.build(0, 0, n-1, nums)
    
    def combine(self, t1, t2):
        nn1, ny1, yn1, yy1 = t1
        nn2, ny2, yn2, yy2 = t2
        nn = max(nn1 + yn2, nn1 + nn2, ny1 + nn2)
        ny = max(nn1 + yy2, nn1 + ny2, ny1 + ny2)
        yn = max(yn1 + yn2, yn1 + nn2, yy1 + nn2)
        yy = max(yn1 + yy2, yn1 + ny2, yy1 + ny2)
        return [nn, ny, yn, yy]
    
    def build(self, i, l, r, nums):
        if l == r:
            self.ar[i] = [0, inf, inf, nums[l]]
        else:
            m = (l+r) // 2
            self.build(2*i+1, l, m, nums)
            self.build(2*i+2, m+1, r, nums)
            self.ar[i] = self.combine(self.ar[2*i+1], self.ar[2*i+2])
        
    def update_v(self, i, l, r, idx, v):
        if l == r and l == idx:
            self.ar[i] = [0, inf, inf, v]
        else:
            m = (l+r)//2
            if m < idx:
                self.update_v(2*i+2, m+1, r, idx, v)
            else:
                self.update_v(2*i+1, l, m, idx, v)
            self.ar[i] = self.combine(self.ar[2*i+1], self.ar[2*i+2])

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        M = 10**9 + 7
        st = SegTree(nums)
        n = len(nums)
        res = 0
        # print(st.ar)
        for p, v in queries:
            st.update_v(0, 0, n-1, p, v)
            # print(st.ar)
            res += max(st.ar[0])
            res %= M
        return res