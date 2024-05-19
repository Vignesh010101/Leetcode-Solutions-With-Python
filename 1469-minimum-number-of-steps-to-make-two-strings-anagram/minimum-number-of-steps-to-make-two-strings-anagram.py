class Solution:
    def minSteps(self, s: str, t: str) -> int:
        res = 0
        
        for  v in set(s):
            num_t = t.count(v)
            num_s = s.count(v)
            
            if num_t < num_s: res += (num_s - num_t)

        return res